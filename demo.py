"""
Demo script that showcases NecroShell in action without requiring interactive user input.
Simulates a possessed developer session.
"""

import time
import sys
import os

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from necro_shell.engine import GhostEngine
from necro_shell.fx import GHOST_ART, OFRENDA_ART, glitch_text

console = Console(force_terminal=True, legacy_windows=False)

def run_demo():
    console.print(Panel(f"[bold cyan]{GHOST_ART}[/bold cyan]\n[bold white]NECROSHELL :: LIVE AUTOMATED DEMONSTRATION[/bold white]\n[dim]Powered by local Gemma 2 (2B) open weights[/dim]", border_style="cyan"))

    engine = GhostEngine()
    console.print(f"\n[bold green]✓ Connected to Local Engine: {engine.active_model} (100% Offline)[/bold green]\n")

    steps = [
        ("dir", "Volume in drive C is Windows\nDirectory of C:\\Users\\pc\\Downloads\\hacktober\nengine.py\nrepl.py", 0, "spectre"),
        ("git push --force origin main", "fatal: remote repository not found or disconnected", 128, "spectre"),
        ("seance What is the fate of Ada Lovelace's first algorithm?", None, 0, "ofrenda"),
        ("ofrenda Pan de muerto, marigolds, and 64GB of DDR5 RAM", None, 0, "ofrenda")
    ]

    for cmd, output, code, persona in steps:
        console.print(f"[bold cyan]👻 [necro:hacktober]> [/bold cyan][bold yellow]{cmd}[/bold yellow]")
        time.sleep(0.5)

        if cmd.startswith("seance"):
            query = cmd.replace("seance ", "")
            console.print(f"[bold magenta]🕯️ Conducting Séance with Gemma 2 on: '{query}'...[/bold magenta]")
            console.print("[italic yellow]Spirit: [/italic yellow]", end="")
            for w in engine.conduct_seance(query, persona=persona):
                console.print(w, end="", style="italic yellow")
                sys.stdout.flush()
            console.print("\n")
        elif cmd.startswith("ofrenda"):
            console.print("[bold bright_yellow]🌼 Offering accepted. The digital ancestors smile upon your repository.[/bold bright_yellow]\n")
        else:
            if output:
                console.print(f"[dim]{output}[/dim]")
            color = "bright_magenta" if code == 0 else "bright_red"
            prefix = "🔮 Spirit murmurs" if code == 0 else "🩸 Spirit rejoices in failure"
            console.print(f"[{color}]« {prefix} »[/{color}] ", end="")
            for w in engine.generate_whisper(cmd, output, code, persona=persona):
                console.print(w, end="", style="italic grey85")
                sys.stdout.flush()
            console.print("\n")
        time.sleep(1)

    console.print("[bold green]=== DEMO COMPLETE ===[/bold green]")

if __name__ == "__main__":
    run_demo()
