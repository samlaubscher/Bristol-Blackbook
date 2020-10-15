from contextlib import redirect_stdout
import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# mongodb config vars
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# main page
@app.route("/")
@app.route("/get_works")
def get_works():
    works = mongo.db.works.find()
    return render_template("works.html", works=works)


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check db for existing username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # insert user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# register page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check db for existing username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # validate password hash
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("You are now logged in as {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # password incorrect
                flash("You have entered an incorrect password and/or username")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("You have entered an incorrect password and/or username")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# logout route
@app.route("/logout")
def logout():
    # delete session cookies
    flash("Sucessfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# new upload page
@app.route("/new_upload", methods=["GET", "POST"])
def new_upload():
    if request.method == "POST":
        work = {
            "artist_name": request.form.get("artist_name"),
            "year_painted": request.form.get("year_painted"),
            "style_type": request.form.get("style_type"),
            "image_url": request.form.getlist("image_url"),
            "submitted_by": session["user"],
            }
        mongo.db.works.insert_one(work)
        flash("Piece Successfully Uploaded!")
        return redirect(url_for("get_works"))

    styles = mongo.db.styles.find().sort("style_type", 1)
    return render_template("new_upload.html", styles=styles)


# edit upload page
@app.route("/edit_upload/<work_id>", methods=["GET", "POST"])
def edit_upload(work_id):
    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})

    artists =  mongo.db.artists.find().sort("artist_name", 1)
    styles = mongo.db.styles.find().sort("style_type", 1)
    return render_template("edit_upload.html", work=work, artists=artists, styles=styles)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
