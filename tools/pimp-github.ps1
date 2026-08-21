[CmdletBinding()]
param(
    [switch]$DryRun,
    [bool]$CreateThreatHuntingLab = $true,
    [bool]$ArchiveOldBashTraining = $true
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Require-Command([string]$Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command not found: $Name"
    }
}

function Invoke-Checked([string]$Label, [scriptblock]$Action) {
    if ($DryRun) {
        Write-Host "[DRY] $Label"
        return
    }
    Write-Host "[RUN] $Label"
    & $Action
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
}

function Set-Topics([string]$Repository, [string[]]$Topics) {
    $payload = @{ names = $Topics } | ConvertTo-Json -Compress
    Invoke-Checked "replace topics on $Repository -> $($Topics -join ', ')" {
        $payload | gh api --method PUT -H 'Accept: application/vnd.github+json' "repos/$Repository/topics" --input - | Out-Null
    }
}

function Set-Repo([string]$Repository, [string]$Description, [string]$Homepage, [string[]]$Topics) {
    Invoke-Checked "set metadata on $Repository" {
        $args = @('repo','edit',$Repository,'--description',$Description)
        if ($Homepage) { $args += @('--homepage',$Homepage) }
        & gh @args
    }
    Set-Topics $Repository $Topics
}

Require-Command gh
Require-Command git

gh auth status | Out-Host
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI is not authenticated.' }

$owner = (gh api user --jq '.login').Trim()
if ($owner -ne 'ger1e') {
    throw "Authenticated GitHub account is '$owner'; expected 'ger1e'."
}

$root = (git rev-parse --show-toplevel 2>$null).Trim()
if ($LASTEXITCODE -ne 0 -or -not $root) {
    throw 'Run this from a clone of ger1e/ger1e.'
}
if ($root -match '(?i)[\\/]Windows[\\/]System32(?:[\\/]|$)') {
    throw "Refusing to operate from System32. Re-clone ger1e/ger1e somewhere under your user profile first."
}

$origin = (git -C $root remote get-url origin).Trim()
if ($origin -notmatch '(?i)(github\.com[:/])ger1e/ger1e(?:\.git)?$') {
    throw "Unexpected origin '$origin'. Expected ger1e/ger1e."
}

Set-Repo 'ger1e/ger1e' `
    'Threat hunting, CTI, detection engineering, repository intelligence, and a sanitized security lab.' `
    'https://gergoilly.hu/' `
    @('threat-hunting','cti','detection-engineering','kql','microsoft-sentinel','defender-xdr','cybersecurity')

Set-Repo 'ger1e/personal-site-lp' `
    'Cyberpunk threat-hunting and CTI landing page with the rotund operator cat.' `
    'https://gergoilly.hu/' `
    @('personal-site','cybersecurity','threat-hunting','cti','static-site','vercel','cyberpunk')

Set-Repo 'ger1e/landing-pages' `
    'Experimental and historical landing-page lab; non-production.' `
    '' `
    @('web-design','cyberpunk','experiments','archive')

Set-Repo 'ger1e/godot' `
    'Personal fork of Godot Engine; upstream-derived and not a portfolio project.' `
    '' `
    @('fork','godot')

Set-Repo 'ger1e/learning-bash-scripting-3212393' `
    'LinkedIn Learning Bash course exercises; training history, not portfolio work.' `
    '' `
    @('bash','training','archive')

if ($ArchiveOldBashTraining) {
    $archived = gh repo view 'ger1e/learning-bash-scripting-3212393' --json isArchived --jq '.isArchived'
    if ($archived -ne 'true') {
        Invoke-Checked 'archive old Bash training repository' {
            gh repo archive 'ger1e/learning-bash-scripting-3212393' --yes
        }
    }
}

if ($CreateThreatHuntingLab) {
    gh repo view 'ger1e/threat-hunting-lab' --json nameWithOwner *> $null
    $labExists = ($LASTEXITCODE -eq 0)
    if (-not $labExists) {
        $temp = Join-Path ([IO.Path]::GetTempPath()) ("ger1e-threat-hunting-lab-" + [guid]::NewGuid().ToString('N'))
        if ($DryRun) {
            Write-Host "[DRY] create public repository ger1e/threat-hunting-lab from $root/lab"
        } else {
            New-Item -ItemType Directory -Path $temp | Out-Null
            try {
                Copy-Item -Path (Join-Path $root 'lab\*') -Destination $temp -Recurse -Force
                @'
__pycache__/
*.py[cod]
.env
.env.*
!.env.example
.DS_Store
Thumbs.db
'@ | Set-Content -Path (Join-Path $temp '.gitignore') -Encoding utf8
                @'
# Security policy

This is a sanitized public threat-hunting lab. Do not submit credentials, private telemetry, customer identifiers, proprietary incident data, or live sensitive infrastructure in issues or pull requests.

The KQL examples are starting points for authorized defensive analysis; validate telemetry, false positives, and environmental assumptions before production use.
'@ | Set-Content -Path (Join-Path $temp 'SECURITY.md') -Encoding utf8
                git -C $temp init -b main | Out-Null
                $uid = (gh api user --jq '.id').Trim()
                git -C $temp config user.name 'ger1e'
                git -C $temp config user.email "$uid+ger1e@users.noreply.github.com"
                git -C $temp add .
                git -C $temp commit -m 'feat: publish sanitized threat hunting lab' | Out-Host
                Push-Location $temp
                try {
                    gh repo create 'ger1e/threat-hunting-lab' --public --description 'Sanitized KQL threat hunts, CTI schema, and evidence-first investigation methodology.' --source . --remote origin --push
                    if ($LASTEXITCODE -ne 0) { throw 'Failed to create threat-hunting-lab.' }
                } finally {
                    Pop-Location
                }
            } finally {
                Remove-Item -Path $temp -Recurse -Force -ErrorAction SilentlyContinue
            }
        }
    }

    if ($labExists -or -not $DryRun) {
        Set-Repo 'ger1e/threat-hunting-lab' `
            'Sanitized KQL threat hunts, CTI schema, and evidence-first investigation methodology.' `
            '' `
            @('threat-hunting','kql','microsoft-defender','microsoft-sentinel','cti','detection-engineering','blue-team')
    }
}

Write-Host ''
Write-Host 'Account-level metadata normalization complete.'
Write-Host 'GitHub user-profile pins are currently configured through Customize your pins in the GitHub UI.'
Write-Host 'Recommended pins: threat-hunting-lab, personal-site-lp, ger1e. Leave forks/training unpinned.'
Write-Host 'Profile: https://github.com/ger1e'
