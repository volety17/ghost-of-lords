"""
Lord's Ghost Oracle: MCC Laws Adjudicator
Interactive Terminal Interface.
"""

import sys
import time
from mcc_oracle.engine import query_ghost_stream, DEFAULT_MODEL
from mcc_oracle.indexer import rulebook

BANNER = r"""
  ╔═══════════════════════════════════════════════════════════════════════╗
  ║    🏏  THE GHOST OF LORD'S: SPIRIT OF THE MCC LAWS (Est. 1788)  👻    ║
  ║         Offline Cricket Law Adjudicator powered by Google Gemma 2     ║
  ╚═══════════════════════════════════════════════════════════════════════╝
"""

PRESET_CASES = {
    "1": (
        "The Non-Striker Run Out ('Mankad')",
        "The bowler breaks the stumps at the non-striker's end before releasing the ball because the non-striker left the crease early."
    ),
    "2": (
        "The Timed-Out Controversy (Angelo Mathews case)",
        "The incoming batsman arrives on the field within 2 minutes, but his helmet chinstrap snaps before taking guard, causing a delay of over 3 minutes. The bowling captain appeals for Timed Out."
    ),
    "3": (
        "The Keeper's Grounded Helmet Incident",
        "The batsman plays an edge, and the ball deflects off the wicketkeeper's spare helmet resting on the grass behind him. The fielder then dives and catches the ball before it touches the turf."
    ),
    "4": (
        "The Jonny Bairstow Ashes Stumping",
        "The batsman ducks under a bouncer, taps his crease, and immediately walks out of his crease to talk to the non-striker under the assumption the over is over. The keeper throws the ball and breaks the stumps."
    )
}

def stream_verdict(scenario: str):
    print("\n" + "=" * 70)
    print("📜 SUMMONING THE GHOST ARBITER OF 1788...")
    print("=" * 70 + "\n")
    
    # Stream token by token
    for chunk in query_ghost_stream(scenario):
        sys.stdout.write(chunk)
        sys.stdout.flush()
    print("\n\n" + "=" * 70 + "\n")

def main():
    print(BANNER)
    print(f"🏛️ Loaded {len(rulebook.laws_2019)} MCC Laws (2019 Code) & Lord's 1788 Founding Records.")
    print(f"🔮 Engine: Google Gemma 2 ({DEFAULT_MODEL}) via Ollama [100% Offline]")
    print("-" * 73)

    while True:
        print("\nCHOOSE AN OPTION:")
        print("  [1] Preset: The Mankad / Non-striker Run Out")
        print("  [2] Preset: Angelo Mathews Timed-Out (Broken strap)")
        print("  [3] Preset: Ball hitting Keeper's Helmet on grass")
        print("  [4] Preset: Bairstow Ashes Crease Walkout Stumping")
        print("  [5] Enter your own Custom Cricket Scenario / Law Dispute")
        print("  [q] Depart the Long Room (Quit)")
        
        choice = input("\nYour verdict, Umpire? > ").strip().lower()
        
        if choice in ("q", "quit", "exit"):
            print("\n*The spectral arbiter fades back into the Lord's pavilion portraits... Fare thee well!* 👻🏏")
            break
        elif choice in PRESET_CASES:
            title, scenario = PRESET_CASES[choice]
            print(f"\n--- Adjudicating Case: {title} ---")
            print(f"Scenario: \"{scenario}\"")
            stream_verdict(scenario)
        elif choice == "5":
            scenario = input("\nEnter the exact scenario or dispute:\n> ").strip()
            if scenario:
                stream_verdict(scenario)
        else:
            print("[!] Please select a valid option (1-5 or q).")

if __name__ == "__main__":
    main()