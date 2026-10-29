import random
import time
import sys

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from rich.console import Console
from rich.text import Text

console = Console(force_terminal=True, legacy_windows=False)

GHOST_ART = r"""
     .-.
   .'   `.
  :       :
  : O   O :
   `.   .'
     ) (
   .'   `.
  /       \
 (  .---.  )
  `'     `'
"""

OFRENDA_ART = r"""
        🕯️  🕯️  🕯️
      .-''''''''-.
    .'  💀    💀  `.
   :    (  ..  )    :
   :     `----'     :
    `.  🌺 🌼 🌸  .'
      `-........-'
       🕯️  🕯️  🕯️
"""

CYBER_SKULL = r"""
    .---.
   /     \
  | () () |  [ERR: MEM_CORRUPT]
   \  ^  /
    |||||
"""

ZALGO_CHARS = [
    '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307',
    '\u0308', '\u0309', '\u030a', '\u030b', '\u030c', '\u030d', '\u030e', '\u030f',
    '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315'
]

def glitch_text(text: str, intensity: float = 0.15) -> str:
    """Randomly corrupts text with diacritics / zalgo characters."""
    result = []
    for char in text:
        result.append(char)
        if char.isalpha() and random.random() < intensity:
            for _ in range(random.randint(1, 3)):
                result.append(random.choice(ZALGO_CHARS))
    return "".join(result)

def typewriter_print(text: str, style: str = "bold green", delay: float = 0.015):
    """Prints text in a spooky typewriter fashion."""
    for char in text:
        console.print(char, style=style, end="")
        sys.stdout.flush()
        time.sleep(delay)
    console.print()

def trigger_spectral_flicker():
    """Flickers the terminal screen briefly like a haunted CRT monitor."""
    for _ in range(2):
        console.clear()
        time.sleep(0.04)
