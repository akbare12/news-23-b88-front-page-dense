#!/usr/bin/env python3
"""news-23 b88 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only (no PIL). Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import binascii
import hashlib
import os
import struct
import sys

MAX_BYTES = 1024 * 1024
MIN_BYTES = 10000
EXPECTED_W, EXPECTED_H = 1024, 1024


def fail(msg):
    print("error: " + msg, file=sys.stderr)
    return 1


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is empty")
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir_abs = os.path.abspath(out_dir)
    if out_dir_abs == repo_dir or out_dir_abs.startswith(repo_dir + os.sep):
        return fail("MAKEFUN_OUTPUT_DIR must not be inside the repo")

    src = os.path.join(repo_dir, "entry.png")
    dst = os.path.join(out_dir_abs, "entry.png")
    if os.path.abspath(dst) == os.path.abspath(src):
        return fail("refusing to overwrite the source entry.png")

    with open(src, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        return fail("entry.png exceeds 1 MiB")
    if len(data) < MIN_BYTES:
        return fail("entry.png is suspiciously small")

    # PNG signature
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return fail("not a PNG file")
    # First chunk must be IHDR, 13 bytes
    length, ctype = struct.unpack(">I4s", data[8:16])
    if ctype != b"IHDR" or length != 13:
        return fail("first chunk is not a 13-byte IHDR")
    w, h, depth, ctype_code = struct.unpack(">IIBB", data[16:26])
    if (w, h) != (EXPECTED_W, EXPECTED_H):
        return fail("expected 1024x1024, got %dx%d" % (w, h))
    if depth != 8 or ctype_code not in (2, 6):
        return fail("expected 8-bit RGB/RGBA, got depth=%d type=%d" % (depth, ctype_code))
    ihdr_crc = binascii.crc32(data[12:29]) & 0xFFFFFFFF
    if ihdr_crc != struct.unpack(">I", data[29:33])[0]:
        return fail("IHDR CRC mismatch")

    # Walk chunks: verify CRC of each, require a non-empty IDAT, IEND last, no trailing data
    pos = 8
    seen_idat = False
    last_type = None
    while pos + 8 <= len(data):
        length, ctype = struct.unpack(">I4s", data[pos:pos + 8])
        end = pos + 8 + length + 4
        if end > len(data):
            return fail("truncated chunk %r" % ctype)
        crc_stored = struct.unpack(">I", data[pos + 8 + length:end])[0]
        crc_calc = binascii.crc32(data[pos + 4:pos + 8 + length]) & 0xFFFFFFFF
        if crc_calc != crc_stored:
            return fail("CRC mismatch in chunk %r" % ctype)
        if ctype == b"IDAT" and length > 0:
            seen_idat = True
        if ctype == b"IEND" and length != 0:
            return fail("IEND chunk must be 0 bytes")
        last_type = ctype
        pos = end
    if pos != len(data):
        return fail("trailing data after last chunk")
    if last_type != b"IEND":
        return fail("last chunk is not IEND")
    if not seen_idat:
        return fail("no non-empty IDAT chunk")

    os.makedirs(out_dir_abs, exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(data)
    with open(dst, "rb") as fh:
        back = fh.read()
    if back != data:
        return fail("output does not match source byte-for-byte")
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
