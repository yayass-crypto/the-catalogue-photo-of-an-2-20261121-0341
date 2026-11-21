"""ROTARY X1 — The Catalogue Photo of an Impossible Gadget.

Writes one catalogue photograph (a matte-black smartphone with a polished
brass rotary telephone dial on its screen, a finger mid-dial, and a coiled
vintage telephone cord as the single accessory) to $MAKEFUN_OUTPUT_DIR/entry.png.

Python 3.13 standard library only. No network. Deterministic: the output
bytes are the committed entry.png, copied verbatim, every run.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024

# The entry image lives next to this script in the repository.
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def _png_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk."""
    # PNG signature (8 bytes) + IHDR length (4) + "IHDR" (4) + w/h (4+4).
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.png")

    with open(SOURCE, "rb") as fh:
        data = fh.read()

    # Gate: re-read and validate before writing anything out.
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("error: entry.png is not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: entry.png is {len(data)} bytes, over {MAX_BYTES}",
              file=sys.stderr)
        return 1
    width, height = _png_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"error: entry.png is {width}x{height}, over "
              f"{MAX_DIMENSION}x{MAX_DIMENSION}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)

    # Re-read the written file and confirm it matches the gated source.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        print("error: written entry.png does not match the source",
              file=sys.stderr)
        return 1

    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {out_path}: {width}x{height}, {len(data)} bytes, "
          f"sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
