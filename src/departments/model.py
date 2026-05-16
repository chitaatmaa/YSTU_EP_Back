from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.base_model import Base


class Department(Base):
    """Кафедры."""
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    short_name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    is_actual: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    disciplines = relationship('Discipline', back_populates='department', cascade='all, delete-orphan')
