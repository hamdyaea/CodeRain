#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Lightweight terminal code rain, with bounded output and clean shutdown."""
from __future__ import annotations

import argparse
import secrets
import shutil
import signal
import string
import sys
import time

ALPHABET = string.ascii_letters + string.digits
GREEN = "\033[92m"
RESET = "\033[0m"


def frame(name: str, width: int, color: bool = True) -> str:
    if width < 1:
        raise ValueError("Terminal width must be positive")
    characters = "".join(secrets.choice(ALPHABET) for _ in range(width))
    label = name[:width]
    start = max(0, (width - len(label)) // 2)
    line = characters[:start] + label + characters[start + len(label):]
    return f"{GREEN}{line}{RESET}" if color else line


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", default="", help="Text displayed in the code rain")
    parser.add_argument("--delay", type=float, default=0.07, help="Seconds between frames")
    parser.add_argument("--lines", type=int, default=0, help="Stop after N lines (0: continuous)")
    parser.add_argument("--no-color", action="store_true")
    args = parser.parse_args()
    if not 0.01 <= args.delay <= 5:
        parser.error("--delay must be between 0.01 and 5")
    if args.lines < 0:
        parser.error("--lines must not be negative")
    name = args.name or input("Name to display: ").strip()
    color = not args.no_color and sys.stdout.isatty()
    count = 0
    try:
        while not args.lines or count < args.lines:
            width = min(shutil.get_terminal_size((80, 24)).columns, 250)
            print(frame(name, width, color), flush=True)
            count += 1
            if not args.lines or count < args.lines:
                time.sleep(args.delay)
    except (KeyboardInterrupt, BrokenPipeError):
        return


if __name__ == "__main__":
    main()
