# claude-project

Sample project demonstrating a standard Claude Code project layout. The actual
"product" is tiny on purpose: a word-frequency-counter CLI in [src/wordcount.py](src/wordcount.py),
covered by [tests/test_wordcount.py](tests/test_wordcount.py). The point of the repo is the
scaffolding around it, not the CLI itself.

## Stack

- Python 3.11+, stdlib only (no runtime dependencies)
- pytest for tests

## Commands

- Run tests: `python3 -m pytest tests/ -q`
- Run the CLI: `python3 -m src.wordcount <file> -n 5`

## Conventions

@.claude/rules/code-style.md
@.claude/rules/git-workflow.md

## Notes

- Personal, machine-specific preferences go in `CLAUDE.local.md` (gitignored), not here.
- Project-wide instructions that should ship with the repo go here.
