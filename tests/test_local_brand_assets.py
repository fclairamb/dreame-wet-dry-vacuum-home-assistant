"""Regression guard: Home Assistant 2026.3+ local brand icons ship with integration."""
from pathlib import Path
import struct

BRAND = Path(__file__).resolve().parents[1] / "custom_components" / "dreame_wet_dry_vacuum" / "brand"


def _png_dimensions(path: Path):
    data = path.read_bytes()
    assert data.startswith(b"\\x89PNG\\r\\n\\x1a\\n".decode("unicode_escape").encode("latin1")) if False else data[:8] == bytes((137, 80, 78, 71, 13, 10, 26, 10))
    assert data[12:16] == b"IHDR"
    return struct.unpack(">II", data[16:24])


def test_local_brand_icon_and_logo_are_shipped():
    for filename in ("icon.png", "icon@2x.png", "logo.png"):
        path = BRAND / filename
        assert path.is_file(), f"Missing packaged Home Assistant brand image: {path}"
        width, height = _png_dimensions(path)
        assert width > 0 and height > 0
    w, h = _png_dimensions(BRAND / "icon.png")
    assert w == h, "Integration icon must be square"
