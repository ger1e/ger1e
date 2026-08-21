# GitHub account polish

Most profile/site work in this repository is automated through GitHub Actions. A few account-level mutations are not exposed by the connected GitHub integration used to maintain this repository.

`tools/pimp-github.ps1` performs those supported account-level operations through the authenticated GitHub CLI:

- normalizes descriptions, homepages, and topics for the profile, production site, landing-page archive, Godot fork, and Bash training repository;
- archives the old Bash training repository by default (reversible with `gh repo unarchive`);
- creates `ger1e/threat-hunting-lab` from the sanitized `lab/` directory when it does not already exist;
- normalizes topics/description for the new hunting-lab repository;
- refuses to run from a clone located under Windows `System32`;
- verifies the authenticated GitHub account and repository origin before writing.

## Run

From a normal clone of `ger1e/ger1e` outside `System32`:

```powershell
pwsh -NoProfile -File .\tools\pimp-github.ps1 -DryRun
pwsh -NoProfile -File .\tools\pimp-github.ps1
```

To keep the old Bash training repository unarchived:

```powershell
pwsh -NoProfile -File .\tools\pimp-github.ps1 -ArchiveOldBashTraining:$false
```

## Pins

GitHub documents user-profile pins as a profile UI setting. After the script finishes, open `https://github.com/ger1e`, choose **Customize your pins**, and pin:

1. `threat-hunting-lab`
2. `personal-site-lp`
3. `ger1e`

Leave `godot`, training repositories, and experimental/archive repositories unpinned. Up to six items are supported, but empty slots are preferable to filler.
