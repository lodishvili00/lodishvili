# Flask-Uploads example
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config["UPLOADED_FILES_DEST"] = "uploads"
files = UploadSet("files", extensions=("pdf", "docx", "pptx"))
configure_uploads(app, files)

@app.route("/upload_material", methods=["GET", "POST"])
@login_required
def upload_material():
    if request.method == "POST" and "file" in request.files:
        filename = files.save(request.files["file"])
        # Save the filename to the database along with course details
        return redirect(url_for("course_materials"))
    return render_template("upload_material.html")
