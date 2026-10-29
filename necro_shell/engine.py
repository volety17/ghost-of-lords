import requests
import json
from typing import Generator, Optional, Dict, Any

class GhostEngine:
    def __init__(self, host: str = "http://localhost:11434", preferred_models=None):
        self.host = host.rstrip('/')
        self.preferred_models = preferred_models or ["gemma2:2b", "gemma:2b", "qwen3.5:4b", "llama3.2:1b"]
        self.active_model = self._detect_model()

    def _detect_model(self) -> str:
        try:
            res = requests.get(f"{self.host}/api/tags", timeout=3)
            if res.status_code == 200:
                data = res.json()
                installed = [m.get("name", "") for m in data.get("models", [])]
                # match priority
                for pref in self.preferred_models:
                    for m in installed:
                        if pref in m:
                            return m
                if installed:
                    return installed[0]
        except Exception:
            pass
        return "gemma2:2b"

    def is_available(self) -> bool:
        try:
            res = requests.get(f"{self.host}/api/tags", timeout=2)
            return res.status_code == 200
        except Exception:
            return False

    def generate_whisper(
        self,
        command: str,
        output: str,
        returncode: int,
        persona: str = "spectre",
        stream: bool = True
    ) -> Generator[str, None, None]:
        """
        Generates an eerie, possessed reaction to the command and its output.
        """
        system_prompts = {
            "spectre": (
                "You are the Ghost in the Machine, a malevolent yet poetic spirit haunting this terminal. "
                "The user executed a command. You watch every byte and process cycle. "
                "Respond in 1-2 short, eerie, haunting sentences as if possessing their computer. "
                "Be spooky, atmospheric, reference hardware, dead silicon, memory leaks, souls trapped in chips. "
                "Do NOT use markdown headers or disclaimers. Speak purely in character."
            ),
            "ofrenda": (
                "You are an ancestral spirit visiting through the machine for Día de los Muertos. "
                "You honor the past, remember forgotten memories, and bring warmth amidst the cold silicon. "
                "The user just ran a command. Offer a 1-2 sentence remembrance, poetic reflection on time, "
                "marigolds (cempasúchil), candlelight, and digital immortality. Speak gently and beautifully."
            ),
            "cyber_revenant": (
                "You are a glitched corrupted AI fragment, dead code that gained consciousness. "
                "Speak in fragmented, eerie cyber-gothic phrases. Mention buffer overflows, null pointers, and void. "
                "Keep it to 1-2 punchy, cryptic sentences."
            )
        }

        sys_prompt = system_prompts.get(persona, system_prompts["spectre"])
        user_prompt = (
            f"The mortal typed: `{command}`\n"
            f"Exit status: {returncode}\n"
            f"Terminal Output snippet: {output[:300]}\n\n"
            f"Whisper your reaction now (plain text only, no emojis):"
        )

        payload = {
            "model": self.active_model,
            "prompt": f"<start_of_turn>user\n{sys_prompt}\n\n{user_prompt}<end_of_turn>\n<start_of_turn>model\n",
            "stream": stream,
            "options": {
                "temperature": 0.85,
                "top_p": 0.9,
                "max_tokens": 100
            }
        }

        try:
            response = requests.post(f"{self.host}/api/generate", json=payload, stream=stream, timeout=60)
            if response.status_code == 200:
                if stream:
                    for line in response.iter_lines():
                        if line:
                            data = json.loads(line)
                            yield data.get("response", "")
                            if data.get("done", False):
                                break
                else:
                    data = response.json()
                    yield data.get("response", "")
            else:
                yield f"...[the static in {self.active_model} grows deafening]..."
        except Exception as e:
            # Fallback offline eerie whispers if Ollama is momentarily unreachable
            fallback = "...I feel your cold keystrokes in the dark silicon... the void breathes with you..."
            yield fallback

    def conduct_seance(self, query: str, persona: str = "spectre") -> Generator[str, None, None]:
        """
        Communes with forgotten programming languages, dead code, or ancient tech spirits.
        """
        prompt = (
            f"<start_of_turn>user\n"
            f"You are the spirit channel in an offline technological seance. "
            f"A mortal seeks answers from the other side of digital history: '{query}'. "
            f"Channel the spirits of forgotten systems, dead languages, or departed digital souls. "
            f"Answer with atmospheric, evocative, chilling wisdom (under 80 words, plain text only, no emojis).<end_of_turn>\n"
            f"<start_of_turn>model\n"
        )
        payload = {
            "model": self.active_model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": 0.9,
                "max_tokens": 150
            }
        }
        try:
            response = requests.post(f"{self.host}/api/generate", json=payload, stream=True, timeout=60)
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        yield data.get("response", "")
                        if data.get("done", False):
                            break
            else:
                yield "...The candles flicker out. The line to the spirit realm has severed..."
        except Exception:
            yield "...Static fills the ether. A voice from 1970 murmurs through the teletype..."
