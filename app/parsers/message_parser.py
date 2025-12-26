import re
from typing import Literal, Optional
from app.core.dto import Vacancy
from app.parsers.filters import filter_vacancy

from app.config import TECH_STACK

FIELDS = {
    "position": ["должность", "позиция", "role"],
    "company": ["компания", "работодатель", "employer"],
    "city": ["город", "location", "место", "г. "],
    "employment": ["занятость", "employment", "формат"],
    "salary": ["оплата", "зп", "зарплата", "вилка", "з/п"],
}

CITY_REGEX = re.compile(
    r"(?:г\.?\s*)?(астана|алматы|шымкент|караганда|тараз|атырау|актау)",
    re.IGNORECASE
)

def find_field(text: str, keywords: list[str]):
    for kw in keywords:
        m = re.search(rf"{kw}[:\s]*(.+)", text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None

def find_city(text: str) -> str | None:
    m = CITY_REGEX.search(text)
    if not m:
        return None
    return m.group(1).capitalize()

def find_salary(text: str, keywords: list[str]) -> str | None:
    for kw in keywords:
        m = re.search(
            rf"{kw}\s*[:\-]?\s*(.+)",
            text,
            re.IGNORECASE
        )
        
        if m:
            value = m.group(1).strip()
            value = value.split("\n")[0].strip()
            
            return value
    return None

PHONE_REGEX = re.compile(
    r"(?<!\d)\+[\d\-\s\(\)]{9,18}"
)

TG_REGEX = re.compile(r"@[\w\d_]{3,}")

def normalize_phone(phone: str) -> str:
    return "+" + re.sub(r"[^\d]", "", phone)

def find_contacts(text: str) -> str | None:
    contacts: list[str] = []

    contacts += TG_REGEX.findall(text)

    for match in PHONE_REGEX.findall(text):
        phone = normalize_phone(match)

        if len(phone) < 11 or len(phone) > 15:
            continue

        contacts.append(phone)

    return ", ".join(sorted(set(contacts))) if contacts else None

def find_url(text: str):
    m = re.search(r"(https?://\S+)", text)
    if m:
        return m.group(1).strip()
    return None

def find_tags(text: str):
    tags = re.findall(r"#(\w+)", text.lower())
    if tags:
        return tags
    return None

def extract_stack_section(text: str) -> str | None:
    m = re.search(
        r"(стек технологий|tech stack|технологии)[:\s]*([\s\S]+)",
        text,
        re.IGNORECASE
    )
    if not m:
        return None

    block = m.group(2)

    block = re.split(
        r"\n\s*(требования|условия|обязанности|контакты)",
        block,
        flags=re.IGNORECASE
    )[0]

    return block.lower()

def extract_stack(text: str) -> list[str]:
    text_l = text.lower()
    stack_section = extract_stack_section(text)

    found: set[str] = set()

    for tech, aliases in TECH_STACK.items():
        for alias in aliases:
            if alias in text_l:
                found.add(tech)

            if stack_section and alias in stack_section:
                found.add(tech)

    return sorted(found)

def find_company(text: str) -> str | None:
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    if not lines:
        return None

    first = lines[0]

    m = re.match(r"^([A-ZА-Я][\w\s&.-]{2,50})", first)
    if m:
        return m.group(1).strip()

    m = re.search(r"компания[:\s]+(.+)", text, re.IGNORECASE)
    if m:
        return m.group(1).split("\n")[0].strip()

    return None

def find_employment(text: str) -> str | None:
    text_l = text.lower()

    if any(w in text_l for w in ["оффлайн", "офлайн", "offline"]):
        return "офлайн"

    if any(w in text_l for w in ["удаленка", "удалёнка", "remote"]):
        return "удалёнка"

    if "гибрид" in text_l:
        return "гибрид"

    return None

def parse_vacancy(
    text: str, 
    source_link: Optional[str] = None, 
    whitelist: dict = {},
    blacklist: list[str] = []
) -> Vacancy | None:
    filtered_message = filter_vacancy(text, whitelist, blacklist)
    if not filtered_message:
        return None
    
    position = find_field(text, FIELDS["position"])
    stack = extract_stack(text)
    city = find_city(text)
    company = find_company(text)
    employment = find_employment(text)
    salary = find_salary(text, FIELDS["salary"])
    
    url = find_url(text)
    tags = find_tags(text)
    contacts = find_contacts(text)

    return Vacancy(
        text=text,
        position=position,
        stack=stack,
        city=city,
        company=company,
        employment=employment,
        salary=salary,
        
        url=url,
        tags=tags,
        contacts=contacts,
        source=source_link
    )
