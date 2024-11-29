import os
from dotenv import load_dotenv
from flask import Flask, render_template

from app.views import attendance

app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ["FLASK_SECRET_KEY"]
app.register_blueprint(attendance)


@app.route("/")
def index():
    return render_template("index.html")
