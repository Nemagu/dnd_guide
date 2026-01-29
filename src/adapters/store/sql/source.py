from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from domain.source import Source

from .base import Base


class SourceModel(Base):
    __tablename__ = "source"

    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str]
    name_in_english: Mapped[str] = mapped_column(String(100))

    def to_domain(self):
        return Source(
            source_id=self.id,
            name=self.name,
            description=self.description,
            name_in_english=self.name_in_english,
        )

    @staticmethod
    def from_domain(source: Source) -> "SourceModel":
        return SourceModel(
            id=source.source_id,
            name=source.name,
            description=source.description,
            name_in_english=source.name_in_english,
        )
