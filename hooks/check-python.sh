#!/usr/bin/env bash
# PostToolUse hook: after Edit/Write, syntax-check any .py file that was touched.
set -euo pipefail

input=$(cat)
file_path=$(echo "$input" | python3 -c "import json,sys; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))")

if [[ "$file_path" == *.py ]] && [[ -f "$file_path" ]]; then
  if ! python3 -m py_compile "$file_path" 2>/tmp/pycheck_err; then
    echo "Syntax error in $file_path:" >&2
    cat /tmp/pycheck_err >&2
    exit 2
  fi
fi
