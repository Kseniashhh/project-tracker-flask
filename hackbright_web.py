"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def homepage():
	""" May be a start point with 2 links to add and to search"""




@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html",github=github, first=first, last=last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student_add", methods=["POST"])
def student_add():

	fname = request.form.get("firstname")
	lname = request.form.get("lastname")
	github = request.form.get("github")

	return render_template("student_added.html", fname=firstname.capitalize(), lname=lastname.capitalize(),github=github )



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
