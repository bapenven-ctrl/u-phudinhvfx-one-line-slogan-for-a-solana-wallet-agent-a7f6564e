#!/usr/bin/env python3
"""Write one slogan, one line, to /output/entry.txt.

Deterministic: the same constant text on every run. No network, no
dependencies beyond the standard library. File mode 0644 is achieved
with os.open + os.umask(0o022) -- never os.chmod on /output or the
output file (that fails with PermissionError on the grading server).
"""

import os

# The final slogan, chosen by internal tournament (see konsep.md).
# 16 words, 84 characters, one line: the agent reads the fine print
# (the contract) before any signature, so the user's SOL never has
# to "learn the hard way". Kept as a literal constant so every run
# writes byte-identical output.
SLOGAN = "Your Solana wallet agent reads the fine print so your SOL never learns the hard way."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    data = (SLOGAN + "\n").encode("utf-8")
    fd = os.open(OUTPUT_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
