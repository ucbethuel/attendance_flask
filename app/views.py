from flask import Blueprint, render_template, request, redirect, url_for, flash

# from app import app
# from app.models import Attendee, db

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
    total_attendance = len(attendanceList)
    return render_template("forms/attendView.html", attendance=attendanceList, total_len=total_attendance)


@attendance.route("/process")
def process_form():
    """
    Processes the form from "/view" url of attendance path and redirect to "attendance.view_attendance" route
    """
    lastId = attendanceList[-1]["id"] + 1
    name = request.args.get('name')
    action_button = "Yes" if lastId % 2 == 0 else "No"
    # if name is true and process data and append to mock data.
    if name:
        # db.session.add(Attendee(name=name))
        # db.session.commit()

        attendanceList.append({"id": lastId,
                               "name": name,
                               "action": action_button})
    flash("Recorded successfully", "success")

    return redirect(url_for("attendance.view_attendance"))
