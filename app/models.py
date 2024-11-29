import os
from app.views import attendance
from sqlalchemy.orm import DeclarativeBase as Base, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
attendance.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
attendance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(attendance, model_class=Base)


class Attendee(db.Model):
    __tablename__ = "attendance_table"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)


db.create_all()
