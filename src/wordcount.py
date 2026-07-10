"""Word frequency counter — the sample use case for this project."""
import argparse
import re
from collections import Counter


def count_words(text: str) -> Counter:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return Counter(words)


def top_n(counts: Counter, n: int = 5) -> list[tuple[str, int]]:
    return counts.most_common(n)


def main() -> None:
    parser = argparse.ArgumentParser(description="Count word frequency in a text file.")
    parser.add_argument("file", help="Path to a text file")
    parser.add_argument("-n", type=int, default=5, help="Number of top words to show")
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as f:
        text = f.read()

    for word, count in top_n(count_words(text), args.n):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
