#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117 (Python 3.13, standard library only).

The entry is the finished front-page image stored beside this file as
entry.png. The program copies it byte for byte to the output directory
the grader provides, so two runs always write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"entry.png not found beside {__file__}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
