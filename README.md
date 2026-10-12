# ASCII Art Generator 🎨

Turn any text into big, bold block-letter ASCII art — right in your terminal. Zero dependencies, works offline.

```
##  ## ###### #     #      ###
#  #  #      #     #      #   #
####  ####  #     #      #   #
#  #  #     #     #      #   #
#  #  ###### ##### #####  ###
```

## Features

- Big 5×5 block font covering A–Z, 0–9, and common punctuation
- Custom draw character (`--char @` for a totally different look)
- Adjustable letter spacing
- Optional box border for instant banner vibes
- Save the art to a file with `--save`
- Interactive mode when you run it with no arguments

## Run it in 30 seconds

```bash
python ascii_art.py --text "HELLO"
```

More fun:

```bash
python ascii_art.py --text "BUILD IN PUBLIC" --char "@" --border
python ascii_art.py --text "DAY 17" --save banner.txt
python ascii_art.py          # interactive mode — just type and hit enter
```

Python 3 only. No installs, no setup.

## What I practiced

- Dictionary-based glyph rendering (a mini "font engine")
- `argparse` for a real command-line interface
- String manipulation: padding, joining, and box-drawing
- Writing a tool that's genuinely fun to share with friends

---

*Day 17 · simple build of my daily coding journey — shipping two projects a day. 💻*
