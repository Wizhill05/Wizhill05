#!/usr/bin/env python3
"""
Converts ascii art (plain text) into a colored SVG, with color assigned
PER CHARACTER based on how "dense" that character is (which stands in for
how dark/light that part of the original photo was).

HOW TO CUSTOMIZE COLORS:
  - Change COLOR_LIGHT / COLOR_DARK below for a simple two-color gradient
    (light chars -> COLOR_LIGHT, dense chars -> COLOR_DARK).
  - For full manual control per-character, edit `get_color()` at the bottom:
    it receives (row, col, char, density 0-1) and must return a hex color.
    You could e.g. look up (row, col) in a dict to override specific spots.
"""

import html

INPUT_FILE = "art.txt"
OUTPUT_FILE = "art.svg"

# Light -> dark ramp (roughly by visual "ink" density). Extend if you see
# characters that aren't in here; unknown chars fall back to mid-density.
RAMP = " .`'^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# --- Default gradient endpoints (edit these two hex colors) ---
COLOR_LIGHT = (0, 212, 255)   # cyan  - assigned to light/sparse characters
COLOR_DARK  = (123, 47, 247)  # violet - assigned to dense/dark characters

FONT_SIZE = 6.2      # px, controls overall image size/sharpness
CHAR_W = FONT_SIZE * 0.6   # monospace advance width
LINE_H = FONT_SIZE * 1.0
BG_COLOR = "#0d1117"  # GitHub dark background, so transparent-looking edges blend


def density(ch: str) -> float:
    if ch == " ":
        return 0.0
    idx = RAMP.find(ch)
    if idx == -1:
        return 0.55  # unknown char -> assume mid density
    return idx / (len(RAMP) - 1)


def lerp(a, b, t):
    return a + (b - a) * t


def get_color(row: int, col: int, ch: str, d: float) -> str:
    """Per-character color. Edit this function for full manual control."""
    r = round(lerp(COLOR_LIGHT[0], COLOR_DARK[0], d))
    g = round(lerp(COLOR_LIGHT[1], COLOR_DARK[1], d))
    b = round(lerp(COLOR_LIGHT[2], COLOR_DARK[2], d))
    return f"#{r:02x}{g:02x}{b:02x}"


def build_svg(lines):
    max_len = max(len(l) for l in lines)
    width = max_len * CHAR_W
    height = len(lines) * LINE_H

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.1f} {height:.1f}" '
        f'width="{width:.0f}" height="{height:.0f}">'
    )
    parts.append(f'<rect width="100%" height="100%" fill="{BG_COLOR}"/>')
    parts.append(
        f'<g font-family="SFMono-Regular, Consolas, Menlo, monospace" '
        f'font-size="{FONT_SIZE}" xml:space="preserve">'
    )

    for row, line in enumerate(lines):
        y = (row + 1) * LINE_H - LINE_H * 0.2
        # group consecutive same-color chars into one tspan for smaller file size
        run_color = None
        run_chars = []
        run_start_col = 0

        def flush(col_end):
            nonlocal run_color, run_chars, run_start_col
            if run_chars and run_color is not None:
                text = html.escape("".join(run_chars))
                x = run_start_col * CHAR_W
                parts.append(
                    f'<tspan x="{x:.1f}" y="{y:.1f}" fill="{run_color}">{text}</tspan>'
                )
            run_chars = []

        for col, ch in enumerate(line):
            if ch == " ":
                flush(col)
                run_start_col = col + 1
                run_color = None
                continue
            d = density(ch)
            color = get_color(row, col, ch, d)
            if color != run_color:
                flush(col)
                run_start_col = col
                run_color = color
            run_chars.append(ch)
        flush(len(line))

    parts.append("</g>")
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
    svg = build_svg(lines)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {OUTPUT_FILE} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
