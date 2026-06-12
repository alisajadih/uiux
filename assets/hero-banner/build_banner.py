#!/usr/bin/env python3
"""Build hero banner exports — no text, opaque, RTL-ready."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
PNG = ROOT / "png"
SOURCE = PNG / "hero-banner-source.png"

# crop ratios for standalone graphic (right side of source)
GRAPHIC_CROP = (0.42, 0.0, 1.0, 1.0)  # left, top, right, bottom (fractions)


def resize(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    return img.resize(size, Image.LANCZOS)


def crop_graphic(img: Image.Image) -> Image.Image:
    w, h = img.size
    l, t, r, b = GRAPHIC_CROP
    return img.crop((int(w * l), int(h * t), int(w * r), int(h * b)))


def main() -> None:
    PNG.mkdir(parents=True, exist_ok=True)
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing source: {SOURCE}")

    src = Image.open(SOURCE).convert("RGB")

    exports = [
        ((1440, 500), "hero-banner"),
        ((2880, 1000), "hero-banner@2x"),
        ((1200, 420), "hero-banner-tablet"),
    ]
    for size, name in exports:
        out = PNG / f"{name}.png"
        resize(src, size).save(out, optimize=True)
        print(f"saved {out}")

    graphic = crop_graphic(src)
    for size, name in [((720, 500), "hero-graphic"), ((1440, 1000), "hero-graphic@2x")]:
        out = PNG / f"{name}.png"
        resize(graphic, size).save(out, optimize=True)
        print(f"saved {out}")


if __name__ == "__main__":
    main()
