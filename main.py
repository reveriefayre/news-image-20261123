#!/usr/bin/env python3
"""Entry for make.fun bounty 'Sum up 23 November's world news in one image'.

Writes one image to /output/entry.png by copying the bundled entry.png.
No network, no randomness, no time dependence: both runs write identical bytes.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"

def main() -> None:
    out = Path("/output/entry.png")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SRC, out)
    except OSError:
        out = HERE / "output" / "entry.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SRC, out)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
