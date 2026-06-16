#!/usr/bin/env python3
"""Build hero banner at exact size and brand colors."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
PNG = ROOT / "png"

PRIMARY = (0x00, 0xBB, 0xA7)   # #00BBA7
SECONDARY = (0xAD, 0x46, 0xFF)  # #AD46FF
BANNER_SIZE = (402, 210)
TEXT_ZONE_RATIO = 0.48
GRAPHIC_CROP = (0.40, 0.0, 1.0, 1.0)


def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def gradient_bg(size: tuple[int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size)
    px = img.load()
    for x in range(w):
        t = x / max(w - 1, 1)
        r = lerp(PRIMARY[0], SECONDARY[0], t)
        g = lerp(PRIMARY[1], SECONDARY[1], t)
        b = lerp(PRIMARY[2], SECONDARY[2], t)
        for y in range(h):
            px[x, y] = (r, g, b)
    return img


def build_from_source(source: Path) -> Image.Image:
    w, h = BANNER_SIZE
    base = gradient_bg((w, h))

    raw = Image.open(source).convert("RGBA")
    l, t, r, b = GRAPHIC_CROP
    rw, rh = raw.size
    graphic = raw.crop((int(rw * l), int(rh * t), int(rw * r), int(rh * b)))

    zone_x = int(w * TEXT_ZONE_RATIO)
    zone_w = w - zone_x
    target_h = int(h * 0.96)
    ratio = target_h / graphic.height
    target_w = min(int(graphic.width * ratio), zone_w)
    target_h = int(graphic.height * (target_w / graphic.width))
    graphic = graphic.resize((target_w, target_h), Image.LANCZOS)

    x = zone_x + (zone_w - target_w) // 2
    y = (h - target_h) // 2
    slice_bg = base.crop((x, 0, x + target_w, h))
    composed = slice_bg.copy()
    composed.paste(graphic.convert("RGB"), (0, y), graphic.split()[3])
    base.paste(composed, (x, y))
    return base


def main() -> None:
    PNG.mkdir(parents=True, exist_ok=True)
    source = PNG / "hero-banner-source.png"
    if not source.exists():
        raise FileNotFoundError(source)

    banner = build_from_source(source)
    out = PNG / "hero-banner-402x210.png"
    banner.save(out, optimize=True)
    print(f"saved {out} ({banner.size[0]}x{banner.size[1]})")

    # standalone graphic crop
    g = banner.crop((int(402 * TEXT_ZONE_RATIO), 0, 402, 210))
    g.save(PNG / "hero-graphic-402x210.png", optimize=True)
    print(f"saved {PNG / 'hero-graphic-402x210.png'}")


if __name__ == "__main__":
    main()
