# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About this repo

A learning project for GitHub Actions. All logic lives in `.github/workflows/`. There is no build system, test runner, or application code — workflows are triggered by pushing to GitHub or via `workflow_dispatch`.

## Workflow overview

| File | Trigger branches | Key concepts demonstrated |
|------|-----------------|--------------------------|
| `myFirstWorkflow.yml` | all branches (push + dispatch) | Job dependencies (`needs`), multi-runner jobs (ubuntu/windows/macos), parallel vs. sequential execution |
| `my2ndWorkflow.yml` | all branches (push + dispatch) | `actions/checkout`, artifact upload/download (`upload-artifact`, `download-artifact`), custom download paths |
| `My3rdWorkflow.yml` | `main`, `dev`, `feature-*` (push); `main` (pull_request) | Branch-filtered triggers, PR trigger, intentional `exit 1` in job2 to demonstrate PR failure behavior |

## Workflow patterns

- **Job sequencing**: `needs: job1` makes a job wait for one dependency; `needs: [job1, job2, job3]` waits for multiple.
- **Artifacts**: Job1 uploads artifacts; downstream jobs download them. Each `upload-artifact` step requires a unique `name`. `download-artifact` fetches by that name, optionally into a `path`.
- **Runner selection**: `runs-on: ubuntu-latest` / `windows-latest` / `macos-latest`. Windows steps default to PowerShell; use `shell: pwsh` explicitly when needed.
- **Intentional failure**: `My3rdWorkflow.yml` job2 ends with `run: exit 1` — this is deliberate for PR demo purposes, not a bug.
