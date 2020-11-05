from contextlib import redirect_stdout
import os
from dns.resolver import query
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
    works = list(mongo.db.works.find())
    work = mongo.db.works.find_one({"_id": ObjectId()})
    return render_template("works.html", works=works, work=work)


# search route
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    works = list(mongo.db.works.find({"$text": {"$search": query}}))
    return render_template("works.html", works=works)


# filter routes
@app.route("/filter_artists")
def filter_artists():
    works = list(mongo.db.works.find().sort("artist_name", 1))
    return render_template("works.html", works=works)


@app.route("/filter_styles")
def filter_styles():
    works = list(mongo.db.works.find().sort("style_type", 1))
    return render_template("works.html", works=works)


@app.route("/filter_year")
def filter_year():
    works = list(mongo.db.works.find().sort("year_painted", 1))
    return render_template("works.html", works=works)


# get work page
@app.route("/get_work/<work_id>", methods=["GET", "POST"])
def get_work(work_id):
    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
    return render_template("get_work.html", work=work)


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
    works = list(mongo.db.works.find())
    artists = list(mongo.db.artists.find())

    if session["user"]:
        return render_template(
            "profile.html", username=username, works=works, artists=artists)

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
            "image_url": request.form.get("image_url"),
            "submitted_by": session["user"],
            }
        mongo.db.works.insert_one(work)
        flash("Piece Successfully Uploaded!")
        return redirect(url_for("get_works"))

    artists = mongo.db.artists.find().sort("artist_name", 1)
    styles = mongo.db.styles.find().sort("style_type", 1)
    return render_template("new_upload.html", artists=artists, styles=styles)


# edit upload page
@app.route("/edit_upload/<work_id>", methods=["GET", "POST"])
def edit_upload(work_id):
    if request.method == "POST":
        update_upload = {
            "artist_name": request.form.get("artist_name"),
            "year_painted": request.form.get("year_painted"),
            "style_type": request.form.get("style_type"),
            "image_url": request.form.get("image_url"),
            "submitted_by": session["user"],
            }
        mongo.db.works.update_one({"_id": ObjectId(work_id)}, {"$set": update_upload})
        flash("Piece Successfully Updated!")

    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
    artists =  mongo.db.artists.find().sort("artist_name", 1)
    styles = mongo.db.styles.find().sort("style_type", 1)
    return render_template("edit_upload.html", work=work, artists=artists, styles=styles)


# delete upload
@app.route("/delete_upload/<work_id>")
def delete_upload(work_id):
    mongo.db.works.remove({"_id": ObjectId(work_id)})
    flash("Piece Successfully Deleted!")
    return redirect(url_for("get_works"))


# artists page
@app.route("/get_artists")
def get_artists():
    artists = list(mongo.db.artists.find().sort("artist_name", 1))
    crews = list(mongo.db.artists.find().sort("artist_crews", 1))
    return render_template("artists.html", artists=artists, crews=crews)


# add artist page
@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    if request.method == "POST":
        artist = {
            "artist_name": request.form.get("artist_name"),
            "artist_crews": request.form.getlist("artist_crews"),
            "submitted_by": session["user"]
            }
        mongo.db.artists.insert_one(artist)
        flash("Artist Successfully Added!")
        return redirect(url_for("get_artists"))

    crews = list(mongo.db.crews.find().sort("crew_name", 1))
    return render_template("add_artist.html", crews=crews)


# edit artist page
@app.route("/edit_artist/<artist_id>", methods=["GET", "POST"])
def edit_artist(artist_id):
    if request.method == "POST":
        update_artist = {
            "artist_name": request.form.get("artist_name")
        }
        mongo.db.artists.update_one({"_id": ObjectId(artist_id)}, {"$set": update_artist})
        flash("Artist Successfully Updated!")
        return redirect(url_for("get_artists"))

    artist = mongo.db.artists.find_one({"_id": ObjectId(artist_id)})
    return render_template("edit_artist.html", artist=artist)


# delete artist route
@app.route("/delete_artist/<artist_id>")
def delete_artist(artist_id):
    mongo.db.artists.remove({"_id": ObjectId(artist_id)})
    flash("Artist Successfully Deleted!")
    return redirect(url_for("get_artists"))


# crews page
@app.route("/get_crews")
def get_crews():
    crews = list(mongo.db.crews.find().sort("crew_name", 1))
    return render_template("crews.html", crews=crews)


# get crew page
@app.route("/get_crew/<crew_id>", methods=["GET", "POST"])
def get_crew(crew_id):
    crew = mongo.db.crews.find_one({"_id": ObjectId(crew_id)})
    return render_template("get_crew.html", crew=crew)


# add crew page
@app.route("/add_crew", methods=["GET", "POST"])
def add_crew():
    if request.method == "POST":
        crew = {
            "crew_name": request.form.get("crew_name"),
            "crew_image": request.form.get("crew_image"),
            "submitted_by": session["user"]
            }
        mongo.db.crews.insert_one(crew)
        flash("Crew Successfully Added!")
        return redirect(url_for("get_crews"))

    return render_template("add_crew.html")


# edit crew page
@app.route("/edit_crew/<crew_id>", methods=["GET", "POST"])
def edit_crew(crew_id):
    if request.method == "POST":
        update_crew = {
            "crew_name": request.form.get("crew_name")
        }
        mongo.db.crews.update_one({"_id": ObjectId(crew_id)}, {"$set": update_crew})
        flash("Crew Successfully Updated!")
        return redirect(url_for("get_crews"))

    crew = mongo.db.crews.find_one({"_id": ObjectId(crew_id)})
    return render_template("edit_crew.html", crew=crew)


# delete crew route
@app.route("/delete_crew/<crew_id>")
def delete_crew(crew_id):
    mongo.db.crews.remove({"_id": ObjectId(crew_id)})
    flash("Crew Successfully Deleted!")
    return redirect(url_for("get_crews"))


# styles page
@app.route("/get_styles")
def get_styles():
    styles = list(mongo.db.styles.find().sort("style_type", 1))
    return render_template("styles.html", styles=styles)


# add style page
@app.route("/add_style", methods=["GET", "POST"])
def add_style():
    if session["user"] == "admin":
        if request.method == "POST":
            style = {
                "style_type": request.form.get("style_type")
                }
            mongo.db.styles.insert_one(style)
            flash("Style Successfully Added!")
            return redirect(url_for("get_styles"))

        return render_template("add_style.html")

    return redirect(url_for("get_styles"))


# edit style page
@app.route("/edit_style/<style_id>", methods=["GET", "POST"])
def edit_style(style_id):
    if session["user"] == "admin":
        if request.method == "POST":
            update_style = {
                "style_type": request.form.get("style_type")
            }
            mongo.db.styles.update_one({"_id": ObjectId(style_id)}, {"$set": update_style})
            flash("Style Successfully Updated!")
            return redirect(url_for("get_styles"))

        styles = mongo.db.styles.find_one({"_id": ObjectId(style_id)})
        return render_template("edit_style.html", styles=styles)
    
    return redirect(url_for("get_styles"))


# delete style route
@app.route("/delete_style/<style_id>")
def delete_style(style_id):
    if session["user"] == "admin":
        mongo.db.styles.remove({"_id": ObjectId(style_id)})
        flash("Style Successfully Deleted!")
        return redirect(url_for("get_styles"))

    return redirect(url_for("get_styles"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
