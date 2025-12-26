import re

from app.config import TECH_MIN_SCORE

def normalize(text: str) -> str:
    return (
        text.lower()
        .replace("-", " ")
        .replace("/", " ")
    )

def whitelist_score(text: str, whitelist: dict[str, int]) -> int:
    score = 0
    for word, weight in whitelist.items():
        if word in text:
            score += weight
    return score

def contains_blacklist(text: str, blacklist: list[str]) -> str | None:
    for word in blacklist:
        if re.search(rf"\b{re.escape(word)}\b", text):
            return word
    return None

def filter_vacancy(
    message: str,
    whitelist: dict[str, int],
    blacklist: list[str],
    min_score: int = TECH_MIN_SCORE,
) -> bool:
    text = normalize(message)

    score = whitelist_score(text, whitelist)

    if score < min_score:
        print(f"Whitelist score too low: {score}")
        return False

    black = contains_blacklist(text, blacklist)
    if black and score < min_score + 2:
        print(f"Blacklisted by: {black}")
        return False

    return True
