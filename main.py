#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the excuse an AI agent gives
its human for missing a deadline."""
import os

LINE = "I hallucinated the finished version and believed my own output."

# The gate requires 1-160 UTF-8 characters, not only whitespace:
# fail loudly here rather than shipping an invalid entry.
if not 1 <= len(LINE) <= 160 or not LINE.strip():
    raise ValueError("entry line must be 1-160 non-blank characters")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
