from dataclasses import dataclass
from typing import Optional

@dataclass
class Vacancy:
    text: str
    
    position: Optional[str] = None
    stack: Optional[list[str]] = None
    city: Optional[str] = None
    company: Optional[str] = None
    employment: Optional[str] = None
    salary: Optional[str] = None
    
    url: Optional[str] = None
    tags: Optional[list[str]] = None
    contacts: Optional[str] = None
    source: Optional[str] = None
