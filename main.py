"""news-image-20261124: copy the front-page image to /output/entry.png.

The image is a newspaper front page summing up Tuesday 24 November 2026:
the ICJ Rohingya genocide ruling backed by 14 nations, Nvidia reinstating
Jensen Huang, tankers burning in the Strait of Hormuz, and the Houthi drone
attack on Riyadh's PIF Tower, plus the day's other stories. It is bundled
in the repo as entry.png; this program just copies it, deterministically.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(f"bundled image missing: {SRC}")
    data = SRC.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise ValueError("bundled image is not a PNG")
    if len(data) > MAX_BYTES:
        raise ValueError(f"bundled image too large: {len(data)} bytes")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dest)
    if dest.stat().st_size != len(data):
        raise IOError("copied image size mismatch")


if __name__ == "__main__":
    main()
