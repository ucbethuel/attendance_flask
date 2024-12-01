from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///attendance.db")

session = Session(bind=engine)

