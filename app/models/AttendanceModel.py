# from app.ext.db_config import session, engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.ext.db_config import engine

class Base(DeclarativeBase):
    pass


class AttendanceModel(Base):
    __tablename__ = "attendance"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    rank: Mapped[str]


# Base.metadata.create_all(bind=engine)

