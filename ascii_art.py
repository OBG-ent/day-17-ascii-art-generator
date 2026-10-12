#!/usr/bin/env python3
"""
ASCII Art Generator — Day 17 (simple) of my daily coding journey.

Turn any text into big block-letter ASCII art, right in your terminal.
No dependencies, no internet — just Python 3.

Usage:
    python ascii_art.py --text "HELLO"
    python ascii_art.py --text "BUILD IN PUBLIC" --char "@" --border
    python ascii_art.py --text "DAY 17" --save banner.txt
    python ascii_art.py            (interactive mode)
"""

import argparse

# A 5x5 block font. "#" = filled, " " = empty.
FONT = {
    "A": [" ### ", "#   #", "#####", "#   #", "#   #"],
    "B": ["#### ", "#   #", "#### ", "#   #", "#### "],
    "C": [" ####", "#    ", "#    ", "#    ", " ####"],
    "D": ["#### ", "#   #", "#   #", "#   #", "#### "],
    "E": ["#####", "#    ", "#### ", "#    ", "#####"],
    "F": ["#####", "#    ", "#### ", "#    ", "#    "],
    "G": [" ####", "#    ", "# ###", "#   #", " ####"],
    "H": ["#   #", "#   #", "#####", "#   #", "#   #"],
    "I": ["#####", "  #  ", "  #  ", "  #  ", "#####"],
    "J": ["  ###", "   # ", "   # ", "#  # ", " ##  "],
    "K": ["#   #", "#  # ", "###  ", "#  # ", "#   #"],
    "L": ["#    ", "#    ", "#    ", "#    ", "#####"],
    "M": ["#   #", "## ##", "# # #", "#   #", "#   #"],
    "N": ["#   #", "##  #", "# # #", "#  ##", "#   #"],
    "O": [" ### ", "#   #", "#   #", "#   #", " ### "],
    "P": ["#### ", "#   #", "#### ", "#    ", "#    "],
    "Q": [" ### ", "#   #", "#   #", "#  # ", " ## #"],
    "R": ["#### ", "#   #", "#### ", "#  # ", "#   #"],
    "S": [" ####", "#    ", " ### ", "    #", "#### "],
    "T": ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
    "U": ["#   #", "#   #", "#   #", "#   #", " ### "],
    "V": ["#   #", "#   #", "#   #", " # # ", "  #  "],
    "W": ["#   #", "#   #", "# # #", "## ##", "#   #"],
    "X": ["#   #", "#   #", " # # ", "#   #", "#   #"],
    "Y": ["#   #", "#   #", " # # ", "  #  ", "  #  "],
    "Z": ["#####", "   # ", "  #  ", " #   ", "#####"],
    "0": [" ### ", "#  ##", "# # #", "##  #", " ### "],
    "1": ["  #  ", " ##  ", "  #  ", "  #  ", " ### "],
    "2": [" ### ", "#   #", "   # ", "  #  ", "#####"],
    "3": ["#### ", "    #", " ### ", "    #", "#### "],
    "4": ["#  # ", "#  # ", "#####", "   # ", "   # "],
    "5": ["#####", "#    ", "#### ", "    #", "#### "],
    "6": [" ### ", "#    ", "#### ", "#   #", " ### "],
    "7": ["#####", "   # ", "  #  ", " #   ", " #   "],
    "8": [" ### ", "#   #", " ### ", "#   #", " ### "],
    "9": [" ### ", "#   #", " ####", "    #", " ### "],
    " ": ["     ", "     ", "     ", "     ", "     "],
    "!": ["  #  ", "  #  ", "  #  ", "     ", "  #  "],
    "?": [" ### ", "#   #", "   # ", "     ", "  #  "],
    ".": ["     ", "     ", "     ", "     ", "  #  "],
    ",": ["     ", "     ", "     ", "  #  ", " #   "],
    ":": ["     ", "  #  ", "     ", "  #  ", "     "],
    "-": ["     ", "     ", "#####", "     ", "     "],
    "'": ["  #  ", "  #  ", "     ", "     ", "     "],
    "&": [" ##  ", "#  # ", " ##  ", "#  # ", " ## #"],
}

GLYPH_HEIGHT = 5


def render(text, char="#", spacing=1):
    """Render text into a list of ASCII-art lines."""
    text = text.upper()
    gap = " " * spacing
    lines = [""] * GLYPH_HEIGHT
    for ch in text:
        glyph = FONT.get(ch, FONT[" "])  # unknown chars become spaces
        for i in range(GLYPH_HEIGHT):
            row = glyph[i].replace("#", char)
            lines[i] += row + gap
    return [line.rstrip() for line in lines]


def add_border(lines, border_char="*"):
    """Wrap the art in a box border."""
    width = max(len(line) for line in lines)
    top = border_char * (width + 4)
    boxed = [top]
    for line in lines:
        boxed.append(f"{border_char} {line.ljust(width)} {border_char}")
    boxed.append(top)
    return boxed


def main():
    parser = argparse.ArgumentParser(
        description="Turn text into big block-letter ASCII art."
    )
    parser.add_argument("--text", "-t", help="Text to render (asks interactively if omitted)")
    parser.add_argument("--char", "-c", default="#",
                        help="Character used to draw the letters (default: #)")
    parser.add_argument("--spacing", "-s", type=int, default=1,
                        help="Spaces between letters (default: 1)")
    parser.add_argument("--border", "-b", action="store_true",
                        help="Wrap the art in a box border")
    parser.add_argument("--save", help="Save the art to a file instead of just printing it")
    args = parser.parse_args()

    text = args.text
    if not text:
        text = input("Enter text to turn into ASCII art: ").strip()
    if not text:
        print("Nothing to render. Bye!")
        return

    lines = render(text, char=args.char, spacing=max(0, args.spacing))
    if args.border:
        lines = add_border(lines)

    art = "\n".join(lines)
    print(art)

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            f.write(art + "\n")
        print(f"\nSaved to {args.save}")


if __name__ == "__main__":
    main()
