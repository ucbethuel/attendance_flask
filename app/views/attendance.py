from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.AttendanceModel import AttendanceModel
from app.ext.db_config import session


"""
The attendance path views and logic.
"""

attendance = Blueprint("attendance", __name__, url_prefix="/attendance")

# Mockup data set as List of Dictionary = List[dict()]
attendanceList = [{"id": 1,
                   "name": "Uchenna",
                   "action": "Yes"},
                  {"id": 2,
                   "name": "Benedicta",
                   "action": "No"},
                  {"id": 3,
                   "name": "Anthony",
                   "action": "Yes"}
                  ]


@attendance.route("/")
def index():
    """
    Returns the index page of attendance and display on browser
    """
    return render_template("forms/attendform.html")


@attendance.route("/view")
def view_attendance():
    """
    Returns and Passed the total_len and attendance dictionary 
    """

    db_attendance = session.query(AttendanceModel).all()
    total_attendance = len(db_attendance)
    return render_template("forms/attendView.html", attendance=db_attendance, total_len=total_attendance)


@attendance.route("/process")
def process_form():
    """
    Processes the form from "/view" url of attendance path and redirect to "attendance.view_attendance" route
    """
    # lastId = int(db_attendance["id"])
    name = request.args.get('name')
    action_button = "Corper"
    # if name is true and process data and append to mock data.
    if name:
        session.add(AttendanceModel(name=name,rank = action_button))
        session.commit()

        # db_attendance.append({"id": lastId,
        #                        "name": name,
        #                        "action": action_button})
    flash("Recorded successfully", "success")

    return redirect(url_for("attendance.view_attendance"))
