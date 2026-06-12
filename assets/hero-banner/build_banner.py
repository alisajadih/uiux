#!/usr/bin/env python3
"""Build hero banner PNG exports."""
from __future__ import annotations

import os
from pathlib import Path

import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"
PNG = ROOT / "png"

HEADLINE = "بهترین فرصت های شغلی در انتظار شماست!"

COLOR_TEAL = (0x11, 0x5E, 0x59)
COLOR_PURPLE = (0x8B, 0x5C, 0xF6)
COLOR_WHITE = (255, 255, 255)


def shape_persian(text: str) -> str:
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def gradient_bg(size: tuple[int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size)
    px = img.load()
    for x in range(w):
        t = x / max(w - 1, 1)
        r = lerp(COLOR_TEAL[0], COLOR_PURPLE[0], t)
        g = lerp(COLOR_TEAL[1], COLOR_PURPLE[1], t)
        b = lerp(COLOR_TEAL[2], COLOR_PURPLE[2], t)
        for y in range(h):
            # subtle vertical depth
            vy = y / max(h - 1, 1)
            shade = 1 - (vy * 0.08)
            px[x, y] = (int(r * shade), int(g * shade), int(b * shade))
    return img


def draw_decorations(draw: ImageDraw.ImageDraw, size: tuple[int, int]) -> None:
    w, h = size
    draw.ellipse((-80, -60, 180, 200), fill=(255, 255, 255, 18))
    draw.ellipse((w - 220, h - 180, w + 60, h + 40), fill=(255, 255, 255, 14))
    draw.ellipse((w * 0.55, -40, w * 0.75, 120), fill=(255, 255, 255, 10))


def build_banner(width: int, height: int) -> Image.Image:
    base = gradient_bg((width, height)).convert("RGBA")
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw_decorations(draw, (width, height))
    base = Image.alpha_composite(base, overlay)

    # Illustration on right
    illus_path = PNG / "hero-illustration.png"
    if illus_path.exists():
        illus = Image.open(illus_path).convert("RGBA")
        target_h = int(height * 0.92)
        ratio = target_h / illus.height
        target_w = int(illus.width * ratio)
        illus = illus.resize((target_w, target_h), Image.LANCZOS)
        x = width - target_w + int(width * 0.02)
        y = (height - target_h) // 2
        base.paste(illus, (x, y), illus)

    draw = ImageDraw.Draw(base)
    scale = width / 1440
    font_head = ImageFont.truetype(str(FONTS / "IRANSansX-Bold.ttf"), int(48 * scale))

    margin_x = int(80 * scale)
    max_text_w = int(width * 0.48)
    text_y = int(height * 0.38)

    headline = shape_persian(HEADLINE)

    # Wrap headline into two lines if needed
    words = headline.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), trial, font=font_head)
        if bbox[2] - bbox[0] <= max_text_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    line_height = int(68 * scale)
    for i, line in enumerate(lines):
        draw.text((margin_x, text_y + i * line_height), line, font=font_head, fill=COLOR_WHITE)

    return base.convert("RGB")


def main() -> None:
    PNG.mkdir(parents=True, exist_ok=True)
    for w, h, name in [(1440, 500, "hero-banner"), (2880, 1000, "hero-banner@2x"), (1200, 420, "hero-banner-tablet")]:
        img = build_banner(w, h)
        out = PNG / f"{name}.png"
        img.save(out, optimize=True)
        print(f"saved {out}")


if __name__ == "__main__":
    main()
