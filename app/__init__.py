from flask import Flask, render_template
from app.views.attendance import attendance


app = Flask(__name__)
app.config.from_object("app.ext.config.Config")
app.register_blueprint(attendance)



@app.route("/")
def index():
    return render_template("index.html")