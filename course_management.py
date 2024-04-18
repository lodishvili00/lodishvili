@app.route("/create_course", methods=["GET", "POST"])
@login_required
def create_course():
    if request.method == "POST":
        # Create a new course and save it to the database
        course = Course(title=request.form["title"])
        db.session.add(course)
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("create_course.html")

