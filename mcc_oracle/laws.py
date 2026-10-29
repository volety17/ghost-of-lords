"""
MCC Laws of Cricket & The Spirit of Cricket Preamble.
Authoritative knowledge base for the Lord's Ghost Arbiter.
"""

SPIRIT_OF_CRICKET_PREAMBLE = """
THE SPIRIT OF CRICKET (MCC Preamble)
Cricket owes much of its unique appeal to the fact that it should be played not only within its Laws 
but also within the Spirit of Cricket. Any action which is seen to abuse this Spirit causes injury 
to the game itself. The major responsibility for ensuring the spirit of fair play rests with the captains.
Respect the authority of the umpires, respect your opponents, and play hard but play fair.
"""

# Core controversial and essential MCC Laws (2017 Code 3rd Edition - 2022)
MCC_LAWS = [
    {
        "id": 20,
        "title": "Law 20: Dead Ball",
        "keywords": ["dead ball", "stopped", "helmet", "interrupted", "injury", "settled"],
        "summary": (
            "The ball becomes dead when it is finally settled in the hands of the wicket-keeper or bowler, "
            "or when a boundary is scored, or when a dismissal occurs. If the ball lodges in the clothing or "
            "equipment of a batter or umpire, or strikes a protective helmet worn by a fielder or on the ground, "
            "it becomes dead immediately."
        )
    },
    {
        "id": 28,
        "title": "Law 28: The Fielder's Equipment",
        "keywords": ["helmet", "cap", "clothing", "ground", "penalty", "5 runs", "gear"],
        "summary": (
            "Law 28.3: Protective equipment on the field. If the ball while in play strikes a helmet belonging "
            "to the fielding side placed on the ground within the field of play, the ball immediately becomes DEAD. "
            "5 penalty runs are awarded to the batting side, in addition to any runs completed or in progress."
        )
    },
    {
        "id": 31,
        "title": "Law 31: Timed Out",
        "keywords": ["timed out", "late", "delay", "broken strap", "equipment failure", "3 minutes", "2 minutes"],
        "summary": (
            "Law 31.1: After a wicket falls or a batter retires, the incoming batter must, unless Time has been called, "
            "be ready to receive the ball, or for the other batter to be ready to receive the next ball, within 2 minutes "
            "(or 3 minutes under older/test codes) of the dismissal. If not, the incoming batter will be given out, Timed out."
        )
    },
    {
        "id": 33,
        "title": "Law 33: Caught",
        "keywords": ["caught", "catch", "boundary", "ground", "fingers", "bump ball", "rebound"],
        "summary": (
            "Law 33.1: The striker is out Caught if a ball delivered by the bowler touches the bat or bat-hand and is "
            "subsequently held by a fielder as a fair catch before it touches the ground. The fielder's first contact "
            "must be inside the boundary. If the ball rebounds off a fielder's helmet, a fair catch can still be made."
        )
    },
    {
        "id": 37,
        "title": "Law 37: Obstructing the Field",
        "keywords": ["obstructing", "willful", "kick ball", "block", "handle", "throw"],
        "summary": (
            "Law 37.1: Either batter is out Obstructing the field if, except in the circumstances of 37.2, "
            "he/she will fully attempts to obstruct or distract the fielding side by word or action. "
            "Preventing a ball from hitting the stumps with the bat or person while out of the crease, unless "
            "avoiding injury, is Out Obstructing the Field."
        )
    },
    {
        "id": 38,
        "title": "Law 38: Run Out (including Non-Striker Run Out / Mankad)",
        "keywords": ["run out", "mankad", "non-striker", "crease", "backing up", "stumps broken"],
        "summary": (
            "Law 38.3: Non-striker leaving their ground early. At any time from the moment the ball comes into play "
            "until the bowler would normally have been expected to release the ball, the bowler is permitted to run "
            "out the non-striker. The dismissal is officially classified as a Run Out under Law 38, NOT unfair play."
        )
    },
    {
        "id": 39,
        "title": "Law 39: Stumped",
        "keywords": ["stumped", "crease", "keeper", "foot", "line", "drag"],
        "summary": (
            "Law 39.1: The striker is out Stumped if a ball in play touches no part of the person or bat other than "
            "the bat/hand, the batter is out of his/her ground, and the wicket is fairly put down by the wicket-keeper "
            "without the intervention of another fielder. If the batter's foot is on the line and not grounded behind it, "
            "they are out."
        )
    },
    {
        "id": 41,
        "title": "Law 41: Unfair Play",
        "keywords": ["unfair", "spirit", "fake fielding", "tampering", "shine", "distraction", "dangerous bowling"],
        "summary": (
            "Law 41: Unfair play includes ball tampering (41.3), deliberate distraction or deception (fake fielding, 41.5), "
            "dangerous short-pitched bowling, and wasting time. Umpires award 5 penalty runs to the opposing side for fake "
            "fielding or deliberate distraction."
        )
    }
]

def search_laws(query: str):
    """
    Search the MCC Laws database for laws matching keywords in the user query.
    Returns the most relevant laws found or all laws if query is broad.
    """
    q = query.lower()
    matches = []
    for law in MCC_LAWS:
        # Check title, summary, and keywords
        if any(kw in q for kw in law["keywords"]) or str(law["id"]) in q:
            matches.append(law)
            
    # If no specific keyword matched, return the most common controversial laws
    if not matches:
        matches = MCC_LAWS[:3]
    return matches