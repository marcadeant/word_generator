from dataclasses import dataclass, field
from typing import Dict


@dataclass
class WordGenerator:

    language: str = field(default="en")
    data: Dict = field(default={})
    topic: str = field(default="Music")






