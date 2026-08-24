from database.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    email: Mapped[str] = mapped_column(String(100),unique=True)
    type: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(50))

    