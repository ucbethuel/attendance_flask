import os
from app import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass




class AttendanceSheet(db.Model):
    __tablename__ = "attendance_table"
    id = db.Column(db.Integer, primary_key = True)


class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)


db.create_all()