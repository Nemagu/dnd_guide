from dataclasses import dataclass
from uuid import UUID


@dataclass
class SimpleSource:
    source_id: UUID
    name: str
    name_in_english: str


@dataclass
class DetailSource(SimpleSource):
    description: str
