from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    #setting up Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False #to supress warning
    SQLALCHEMY_DATABASE_URI = "sqlite:///attendance.db"
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"] or "ucbethuel"
    