# Agent instructions

## Purpose
This repository exists only to test the Agent Bridge PoC between ChatGPT Work, GitHub, and Codex.

## Operating rules
1. Work only inside this repository and only on the explicitly assigned task.
2. Inspect the repository before editing.
3. Prefer the smallest correct change.
4. Run all relevant tests after changes. If a test fails, investigate and iterate before reporting completion.
5. Do not weaken, delete, or bypass tests merely to obtain a passing result.
6. Do not introduce dependencies unless the task explicitly requires them.
7. Do not access or modify any other repository, especially AI-Tax-Agent or other production work.
8. Never add secrets, credentials, tokens, personal data, or production data.
9. Do not merge, release, delete data, rewrite history, or make architecture/security-policy changes without explicit human approval.
10. At the end of each task, report: status, files changed, tests run and results, risks/limitations, and whether human approval is required.

## Completion states
Use exactly one of these states in the final task report:
- `PASS` — task completed and verification passed.
- `BLOCKED` — task cannot safely continue without missing information or capability.
- `HUMAN_REQUIRED` — a protected decision/action requires human approval.
- `FAIL` — task was attempted but verification failed.

## Test application
The application in this repository must remain deliberately trivial. Complexity belongs in the bridge protocol, not in the demo application.
