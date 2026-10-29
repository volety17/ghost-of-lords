import sys
import os
import argparse
import time

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from necro_shell.engine import GhostEngine
from necro_shell.executor import execute_system_command
from necro_shell.fx import (
    GHOST_ART, OFRENDA_ART, CYBER_SKULL,
    glitch_text, typewriter_print, trigger_spectral_flicker
)

console = Console(force_terminal=True, legacy_windows=False)

class NecroShellREPL:
    def __init__(self, persona: str = "spectre", model: str = None):
        self.persona = persona
        self.engine = GhostEngine()
        if model:
            self.engine.active_model = model
        self.running = True
        self.possession_level = 1  # Escalates as more commands are run!
        self.ofrendas_offered = []

    def print_banner(self):
        banner_text = Text()
        if self.persona == "ofrenda":
            art = OFRENDA_ART
            title = "🕯️ OFRENDA SHELL :: MEMORIAS DEL SILICIO 🕯️"
            subtitle = "Día de los Muertos Edition - Honoring Digital Ancestors & Open Weights"
            color = "bright_yellow"
        elif self.persona == "cyber_revenant":
            art = CYBER_SKULL
            title = "⚠️ REVENANT.SYS :: CORRUPTED HEURISTIC ⚠️"
            subtitle = "A phantom kernel process trapped in memory cycles"
            color = "bright_red"
        else:
            art = GHOST_ART
            title = "👻 NECROSHELL :: THE GHOST IN THE MACHINE 👻"
            subtitle = "A Haunted POSIX/PowerShell Terminal Possessed by Gemma"
            color = "bright_cyan"

        banner_text.append(f"{art}\n", style=f"bold {color}")
        banner_text.append(f"{title}\n", style="bold underline white")
        banner_text.append(f"{subtitle}\n", style="italic grey70")
        banner_text.append(f"Entity Core: {self.engine.active_model} | Status: 100% OFFLINE & LOCAL\n", style="bold magenta")
        banner_text.append(f"Type 'help', 'seance <query>', 'ofrenda <item>', 'exorcise', or any terminal command.\n", style="dim")

        console.print(Panel(banner_text, border_style=color, expand=False))

    def handle_special_command(self, cmd: str) -> bool:
        cmd_clean = cmd.strip()
        parts = cmd_clean.split(maxsplit=1)
        action = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if action in ("exit", "quit"):
            console.print("\n[bold red]...The machine spirit dissolves back into cold transistors... Goodbye mortal...[/bold red]")
            self.running = False
            return True

        if action == "help":
            self.show_help()
            return True

        if action == "clear" or action == "cls":
            console.clear()
            return True

        if action == "seance":
            self.run_seance(arg)
            return True

        if action == "ofrenda":
            self.offer_ofrenda(arg)
            return True

        if action == "exorcise":
            self.run_exorcism()
            return True

        if action == "necro-manifest":
            trigger_spectral_flicker()
            console.print(Panel(f"[bold red]{GHOST_ART}[/bold red]\n[italic]I AM BINDED TO YOUR SILICON.[/italic]"))
            return True

        if action == "persona":
            if arg in ["spectre", "ofrenda", "cyber_revenant"]:
                self.persona = arg
                console.print(f"[bold green]Entity shifted to persona: [italic]{arg}[/italic][/bold green]")
            else:
                console.print("[yellow]Available personas: spectre, ofrenda, cyber_revenant[/yellow]")
            return True

        return False

    def show_help(self):
        table = Table(title="🕯️ NecroShell Sacred Invocations 🕯️", border_style="cyan")
        table.add_column("Command", style="bold yellow")
        table.add_column("Effect", style="white")

        table.add_row("seance <query>", "Commune with departed code, dead languages, or ancestral systems")
        table.add_row("ofrenda <offering>", "Place an offering (CPU cycles, flowers, pan de muerto) on the digital altar")
        table.add_row("persona <type>", "Shift the haunting spirit: spectre | ofrenda | cyber_revenant")
        table.add_row("necro-manifest", "Force the spirit to visually manifest on your terminal screen")
        table.add_row("exorcise", "Attempt to cleanse the machine's cache (temporarily lowers possession)")
        table.add_row("<any system command>", "Runs dir, git, ls, cat, etc., and triggers an eerie AI reaction")
        table.add_row("exit / quit", "Break the circle and exit to mortal shell")
        console.print(table)

    def run_seance(self, query: str):
        if not query:
            query = "the forgotten souls of punch-card programmers"
        console.print(f"\n[bold magenta]🕯️ Lighting virtual candles... Channeling the spirit realm regarding: '{query}'...[/bold magenta]")
        console.print("[italic cyan]Gemma Spirit Whisper:[/italic cyan] ", end="")
        for token in self.engine.conduct_seance(query, persona=self.persona):
            console.print(token, end="", style="bold yellow")
            sys.stdout.flush()
        console.print("\n")

    def offer_ofrenda(self, item: str):
        if not item:
            item = "Cempasúchil flowers and hot chocolate"
        self.ofrendas_offered.append(item)
        self.possession_level = max(1, self.possession_level - 1)
        console.print(f"\n[bold bright_yellow]🌼 OFRENDA PLACED: '{item}'[/bold bright_yellow]")
        console.print("[italic dim]The digital spirits accept your remembrance. The silicon warms with peace.[/italic dim]\n")

    def run_exorcism(self):
        console.print("[bold red]⚡ INITIATING EXORCISM PROTOCOL... FLUSHING CACHE... ⚡[/bold red]")
        time.sleep(0.5)
        self.possession_level = 1
        console.print("[bold green]✓ The spirits retreat into the shadows... for now.[/bold green]\n")

    def start(self):
        self.print_banner()

        while self.running:
            try:
                cwd = os.getcwd()
                short_cwd = os.path.basename(cwd) or cwd

                # Prompt styling depends on persona
                if self.persona == "ofrenda":
                    prompt_str = f"🌼 [ofrenda:{short_cwd}]🕯️> "
                elif self.persona == "cyber_revenant":
                    prompt_str = f"💀 [REV_LVL_{self.possession_level}:{short_cwd}]#> "
                else:
                    prompt_str = f"👻 [necro:{short_cwd}]👻> "

                # Possessed glitch occasionally on prompt
                if self.possession_level > 3:
                    prompt_str = glitch_text(prompt_str, intensity=0.08)

                user_input = console.input(f"[bold cyan]{prompt_str}[/bold cyan]")
                if not user_input.strip():
                    continue

                # Check built-in possessed commands
                if self.handle_special_command(user_input):
                    continue

                # Execute real system command
                retcode, output = execute_system_command(user_input)

                # Print command output if any
                if output:
                    console.print(output)

                # The Ghost in the Machine whispers!
                self.possession_level += 1
                color = "bright_magenta" if retcode == 0 else "bright_red"
                prefix = "🔮 Spirit murmurs" if retcode == 0 else "🩸 Spirit rejoices in failure"

                console.print(f"\n[{color}]« {prefix} »[/{color}] ", end="")
                for chunk in self.engine.generate_whisper(user_input, output, retcode, persona=self.persona):
                    console.print(chunk, end="", style="italic grey85")
                    sys.stdout.flush()
                console.print("\n")

            except (KeyboardInterrupt, EOFError):
                console.print("\n[dim]Séance interrupted. Exiting...[/dim]")
                break

def main():
    parser = argparse.ArgumentParser(description="NecroShell: The Ghost in the Machine")
    parser.add_argument("--persona", choices=["spectre", "ofrenda", "cyber_revenant"], default="spectre", help="Spirit persona")
    parser.add_argument("--model", type=str, default=None, help="Specific Ollama model to use (default: gemma2:2b)")
    args = parser.parse_args()

    shell = NecroShellREPL(persona=args.persona, model=args.model)
    shell.start()

if __name__ == "__main__":
    main()
