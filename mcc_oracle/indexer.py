"""
MCC Laws Indexer & Retriever for offline AI adjudication.
Parses full 42 Laws of Cricket (2019) and the 1788 founding code.
"""

import os
import re
from typing import Dict, List, Tuple

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_2019 = os.path.join(CURRENT_DIR, "laws_2019.txt")
FILE_1788 = os.path.join(CURRENT_DIR, "laws_1788.txt")


class MCCRulebook:
    def __init__(self):
        self.laws_2019 = self._load_and_split_2019()
        self.laws_1788 = self._load_1788()

    def _load_and_split_2019(self) -> Dict[int, Dict[str, str]]:
        """Parses the full 42 MCC laws into structured sections."""
        if not os.path.exists(FILE_2019):
            return {}

        with open(FILE_2019, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        # Split on LAW X (e.g., LAW 1, LAW 2, ... LAW 42)
        pattern = r"\bLAW\s+(\d+)\s+([A-Z\s,'\-\(\)]+)(?=\n|$)"
        splits = list(re.finditer(pattern, text))
        
        laws = {}
        for i, match in enumerate(splits):
            law_num = int(match.group(1))
            title = match.group(0).strip()
            start_pos = match.end()
            end_pos = splits[i + 1].start() if i + 1 < len(splits) else len(text)
            content = text[start_pos:end_pos].strip()
            
            # Avoid duplicate law index overwrites
            if law_num not in laws or len(content) > len(laws[law_num]["content"]):
                laws[law_num] = {
                    "number": law_num,
                    "title": title,
                    "content": content
                }
        return laws

    def _load_1788(self) -> str:
        """Loads the ancestral 1788 founding code of Lord's."""
        if not os.path.exists(FILE_1788):
            return "The 1788 Code was not found."
        with open(FILE_1788, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().strip()

    def search(self, query: str, top_k: int = 2) -> List[Tuple[int, str, str]]:
        """
        Keyword & token-frequency match across all 42 MCC laws.
        Returns top matching laws: (law_number, law_title, excerpt).
        """
        query_words = set(re.findall(r"\w+", query.lower()))
        
        # Stop words to ignore
        stop_words = {"the", "a", "an", "is", "and", "or", "in", "on", "of", "to", "what", "can", "if"}
        query_words = {w for w in query_words if w not in stop_words and len(w) > 2}

        # Check if user specifically requested a law number (e.g. "Law 38" or "Rule 31")
        num_match = re.search(r"\b(?:law|rule)\s*(\d+)\b", query, re.I)
        forced_law = int(num_match.group(1)) if num_match else None

        scores = []
        for law_num, data in self.laws_2019.items():
            if forced_law and law_num == forced_law:
                score = 9999
            else:
                text_lower = (data["title"] + " " + data["content"]).lower()
                # Score based on how many query terms appear and how frequently
                score = sum(text_lower.count(word) for word in query_words)
                # Boost if query term is in the title
                score += sum(10 for word in query_words if word in data["title"].lower())

            if score > 0:
                scores.append((score, law_num, data["title"], data["content"]))

        scores.sort(key=lambda x: x[0], reverse=True)
        
        results = []
        for _, law_num, title, content in scores[:top_k]:
            # Limit excerpt length so we don't overwhelm Gemma's context window
            excerpt = content[:2500]
            results.append((law_num, title, excerpt))
            
        return results


# Global rulebook instance
rulebook = MCCRulebook()