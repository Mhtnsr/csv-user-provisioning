# Hosted CI validation — November 7, 2026

**Observed result: all jobs passed.**

[Inspect the run](https://github.com/Mhtnsr/csv-user-provisioning/actions/runs/42377614910) · tested source commit: `31928a248621cc17dd92048c0212cec49ce3ead9`.

| Job | Result |
| --- | --- |
| Python 3.12 / windows-latest | success |
| Python 3.10 / windows-latest | success |
| Python 3.10 / ubuntu-latest | success |
| Python 3.12 / ubuntu-latest | success |

## Scope

The suite runs the CSV validator against synthetic inputs; it does not provision accounts.

These are GitHub-hosted runner results. They are not evidence of a personal home-lab build, an employer deployment, or a resolved customer incident. Later runs can have different results; inspect the [workflow history](https://github.com/Mhtnsr/csv-user-provisioning/actions/workflows/checks.yml) for current status.

## What changed during setup

The first PowerShell workflow definition failed validation because a matrix expression was not supported in the shell field. It was changed to two explicit runtime jobs; the linked run is the corrected passing result. The Python workflows passed their first runs.
