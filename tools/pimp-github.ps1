[CmdletBinding()]
param(
    [switch]$DryRun,
    [bool]$CreateThreatHuntingLab = $true,
    [bool]$ArchiveOldBashTraining = $true,
    [bool]$ArchiveGodot = $true,
    [bool]$ArchiveLandingPages = $true,
    [bool]$ConfigureGovernance = $true
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

function Test-RepoArchived([string]$Repository) {
    $value = (& gh repo view $Repository --json isArchived --jq '.isArchived').Trim()
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to read archive state for $Repository"
    }
    return ($value -eq 'true')
}

function Set-Topics([string]$Repository, [string[]]$Topics) {
    $payload = @{ names = $Topics } | ConvertTo-Json -Compress
    Invoke-Checked "replace topics on $Repository -> $($Topics -join ', ')" {
        $payload | gh api --method PUT -H 'Accept: application/vnd.github+json' -H 'X-GitHub-Api-Version: 2026-03-10' "repos/$Repository/topics" --input - | Out-Null
    }
}

function Set-Repo([string]$Repository, [string]$Description, [string]$Homepage, [string[]]$Topics) {
    if (Test-RepoArchived $Repository) {
        Write-Host "[SKIP] metadata on archived repository $Repository"
        return
    }

    Invoke-Checked "set metadata on $Repository" {
        & gh repo edit $Repository --description $Description --homepage $Homepage
    }
    Set-Topics $Repository $Topics
}

function Archive-Repo([string]$Repository) {
    if (Test-RepoArchived $Repository) {
        Write-Host "[SKIP] $Repository is already archived"
        return
    }

    Invoke-Checked "archive $Repository" {
        gh repo archive $Repository --yes
    }
}

function Set-RepositoryPolicy([string]$Repository) {
    $payload = @{
        allow_squash_merge     = $true
        allow_merge_commit     = $false
        allow_rebase_merge     = $false
        allow_auto_merge       = $true
        delete_branch_on_merge = $true
        allow_update_branch    = $true
        has_wiki               = $false
        has_projects           = $false
    } | ConvertTo-Json -Compress

    Invoke-Checked "normalize merge/features policy on $Repository" {
        $payload | gh api --method PATCH -H 'Accept: application/vnd.github+json' -H 'X-GitHub-Api-Version: 2026-03-10' "repos/$Repository" --input - | Out-Null
    }
}

function Set-WorkflowPolicy([string]$Repository, [bool]$AllowPullRequestAutomation) {
    $payload = @{
        default_workflow_permissions = 'read'
        can_approve_pull_request_reviews = $AllowPullRequestAutomation
    } | ConvertTo-Json -Compress

    Invoke-Checked "set least-privilege Actions defaults on $Repository" {
        $payload | gh api --method PUT -H 'Accept: application/vnd.github+json' -H 'X-GitHub-Api-Version: 2026-03-10' "repos/$Repository/actions/permissions/workflow" --input - | Out-Null
    }
}

function Set-BranchProtection([string]$Repository, [string[]]$Contexts) {
    $payload = @{
        required_status_checks = @{
            strict = $true
            contexts = $Contexts
        }
        enforce_admins = $true
        required_pull_request_reviews = @{
            dismiss_stale_reviews = $true
            require_code_owner_reviews = $false
            required_approving_review_count = 0
            require_last_push_approval = $false
        }
        restrictions = $null
        required_linear_history = $true
        allow_force_pushes = $false
        allow_deletions = $false
        block_creations = $false
        required_conversation_resolution = $true
        lock_branch = $false
        allow_fork_syncing = $true
    } | ConvertTo-Json -Depth 6 -Compress

    Invoke-Checked "protect $Repository/main -> $($Contexts -join ', ')" {
        $payload | gh api --method PUT -H 'Accept: application/vnd.github+json' -H 'X-GitHub-Api-Version: 2026-03-10' "repos/$Repository/branches/main/protection" --input - | Out-Null
    }
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

Set-Repo 'ger1e/cti-enrichment-gateway' `
    'Bounded read-only CTI enrichment gateway with evidence-v2 provenance, STIX 2.1, Maltego and deterministic reporting.' `
    'https://gergoilly.hu/' `
    @('cybersecurity','cti','threat-intelligence','threat-hunting','osint','stix','maltego','detection-engineering','nodejs','vercel')

Set-Repo 'ger1e/personal-site-lp' `
    'Static-first security portfolio for threat hunting, CTI and detection engineering — gergoilly.hu.' `
    'https://gergoilly.hu/' `
    @('personal-site','cybersecurity','threat-hunting','cti','static-site','vercel','cyberpunk')

Set-Repo 'ger1e/landing-pages' `
    'Experimental and historical landing-page lab; non-production.' `
    '' `
    @('web-design','cyberpunk','experiments','archive')

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
            'https://gergoilly.hu/' `
            @('threat-hunting','kql','microsoft-defender','microsoft-sentinel','cti','detection-engineering','blue-team')
    }
}

if ($ArchiveLandingPages) { Archive-Repo 'ger1e/landing-pages' }
if ($ArchiveGodot) { Archive-Repo 'ger1e/godot' }
if ($ArchiveOldBashTraining) { Archive-Repo 'ger1e/learning-bash-scripting-3212393' }

if ($ConfigureGovernance) {
    $activeRepos = @(
        'ger1e/ger1e',
        'ger1e/cti-enrichment-gateway',
        'ger1e/personal-site-lp',
        'ger1e/threat-hunting-lab'
    )

    foreach ($repo in $activeRepos) {
        Set-RepositoryPolicy $repo
    }

    Set-WorkflowPolicy 'ger1e/ger1e' $true
    Set-WorkflowPolicy 'ger1e/cti-enrichment-gateway' $false
    Set-WorkflowPolicy 'ger1e/personal-site-lp' $false
    Set-WorkflowPolicy 'ger1e/threat-hunting-lab' $false

    Set-BranchProtection 'ger1e/ger1e' @('validate','catalog')
    Set-BranchProtection 'ger1e/cti-enrichment-gateway' @('Tooling smoke')
    Set-BranchProtection 'ger1e/personal-site-lp' @('static-site-qa')
    Set-BranchProtection 'ger1e/threat-hunting-lab' @('validate')
}

Write-Host ''
Write-Host 'MAXX GitHub account finalization complete.'
Write-Host 'Recommended profile pins: cti-enrichment-gateway, threat-hunting-lab, personal-site-lp, ger1e.'
Write-Host 'Legacy repositories should remain archived and unpinned.'
Write-Host 'Profile: https://github.com/ger1e'
