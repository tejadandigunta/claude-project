---
name: word-count
description: Count word frequency in a text file and report the top N words. Use when the user asks to analyze word frequency, find the most common words in a file, or summarize text by word usage.
---

# Word count

1. Confirm the target file path with the user if it wasn't given explicitly.
2. Run: `python3 -m src.wordcount <file> -n <N>` (default N=5).
3. Present the results as a short ranked list (word: count).
4. If the file doesn't exist or is empty, say so instead of guessing content.
