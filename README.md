# claude-project

A minimal example of a Claude Code project layout, built around one tiny
real use case (a word-frequency counter) so every config piece has something
concrete to point at.

## Layout

```
CLAUDE.md                   Shared project instructions (committed)
CLAUDE.local.md             Personal, machine-specific notes (gitignored)
.mcp.json                   Example MCP server config (filesystem)
.claude/
  settings.json             Project settings — permissions + hooks
  rules/                    Modular convention docs, pulled into CLAUDE.md via @imports
    code-style.md
    git-workflow.md
  commands/                 Custom slash commands
    test.md                 /test
    wordcount.md            /wordcount <file> [n]
  skills/
    word-count/SKILL.md      Skill Claude can invoke for word-frequency requests
  hooks/
    check-python.sh          PostToolUse hook: syntax-checks .py files after Edit/Write
src/wordcount.py             The actual use case: word frequency counter
tests/test_wordcount.py      Tests for it
pyproject.toml               pytest config
```

## Try it

```
python3 -m pytest tests/ -q
python3 -m src.wordcount README.md -n 5
```

Or from Claude Code: `/test`, `/wordcount README.md 5`, or just ask
"what are the most common words in README.md?" (routes to the `word-count` skill).
