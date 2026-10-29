"""
MCC Ghost Engine - Connects local Gemma 2 to the MCC Laws Indexer.
100% offline via Ollama.
"""

import json
import urllib.request
import urllib.error
from typing import Dict, Any, Generator
from mcc_oracle.indexer import rulebook

OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma2:2b"

SYSTEM_INSTRUCTION = """You are the Ghost Arbiter of the Marylebone Cricket Club (MCC), haunting the Long Room at Lord's since 1788.
You are the supreme custodian of the Laws of Cricket and the sacred Spirit of Cricket.

When presented with a cricket dispute or scenario:
1. Deliver the **Official MCC Ruling**: State clearly whether the batter is OUT, NOT OUT, or if PENALTY RUNS apply, citing the specific Law provided in the context.
2. Deliver the **Ghost's Verdict on the 'Spirit of Cricket'**: Deliver sharp, atmospheric Victorian gentleman's commentary on the conduct, sportsmanship, and chivalry of the act.
3. Keep your tone dignified, authoritative, slightly spectral, and deeply knowledgeable of cricket lore.
"""

def generate_prompt(scenario: str) -> str:
    """Retrieves relevant laws and constructs the prompt for Gemma 2."""
    matches = rulebook.search(scenario, top_k=2)
    
    context_text = ""
    for law_num, title, excerpt in matches:
        context_text += f"\n--- {title} ---\n{excerpt[:1800]}\n"

    prompt = f"""{SYSTEM_INSTRUCTION}

[OFFICIAL MCC LAWS CONTEXT]
{context_text}

[CRICKET SCENARIO / DISPUTE]
{scenario}

Please provide your ruling now:"""
    return prompt

def query_ghost_stream(scenario: str, model: str = DEFAULT_MODEL) -> Generator[str, None, None]:
    """
    Streams the ghost verdict token-by-token from local Gemma 2.
    """
    prompt = generate_prompt(scenario)
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": 0.3,  # Lower temperature for precise legal adjudication
            "num_predict": 600
        }
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_API_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            for line in response:
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    yield chunk.get("response", "")
                    if chunk.get("done", False):
                        break
    except urllib.error.URLError as e:
        yield f"\n[Spectral Interference: Could not reach Ollama at {OLLAMA_API_URL}. Is Ollama running? Error: {e}]"