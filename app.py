from contextlib import redirect_stdout
import os
from dns.resolver import query
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
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
@app.route("/works")
def works():
    works = list(mongo.db.works.find().sort("date_submitted", -1))
    return render_template("works.html", works=works)


# search route
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    works = list(mongo.db.works.find({"$text": {"$search": query}}))
    return render_template("works.html", works=works)


# filter route
@app.route("/filter/<filter_type>/<direction>")
def filter(filter_type, direction):
    if direction == 'ascending':
        works = list(mongo.db.works.find().sort(filter_type, 1))
        return render_template("works.html", works=works)

    works = list(mongo.db.works.find().sort(filter_type, -1))   
    return render_template("works.html", works=works)


# get work page
@app.route("/work/<work_id>")
def work(work_id):
    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
    return render_template("work.html", work=work)


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


# login page
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
@app.route("/profile/<username>")
def profile(username):
    if session["user"]:
        # get session user's username from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        works = list(mongo.db.works.find())
        artists = list(mongo.db.artists.find())
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


# new work page
@app.route("/new_work", methods=["GET", "POST"])
def new_work():
    if session["user"]:
        if request.method == "POST":
            work = {
                "artist_name": request.form.get("artist_name"),
                "year_painted": request.form.get("year_painted"),
                "style_type": request.form.get("style_type"),
                "image_url": request.form.get("image_url"),
                "submitted_by": session["user"],
                "date_submitted": datetime.now()
                }
            mongo.db.works.insert_one(work)
            flash("Work Successfully Uploaded!")
            return redirect(url_for("works"))

        artists = mongo.db.artists.find().sort("artist_name", 1)
        styles = mongo.db.styles.find().sort("style_type", 1)
        return render_template("new_work.html", artists=artists, styles=styles)

    return redirect(url_for("login"))


# edit work page
@app.route("/edit_work/<work_id>", methods=["GET", "POST"])
def edit_work(work_id):
    if request.method == "POST":
        update_work = {
            "artist_name": request.form.get("artist_name"),
            "year_painted": request.form.get("year_painted"),
            "style_type": request.form.get("style_type"),
            "image_url": request.form.get("image_url"),
            "submitted_by": session["user"],
            }
        mongo.db.works.update_one({"_id": ObjectId(work_id)}, {"$set": update_work})
        flash("Work Successfully Updated!")

    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
    artists =  mongo.db.artists.find().sort("artist_name", 1)
    styles = mongo.db.styles.find().sort("style_type", 1)
    return render_template("edit_work.html", work=work, artists=artists, styles=styles)


# delete work
@app.route("/delete_work/<work_id>")
def delete_work(work_id):
    mongo.db.works.remove({"_id": ObjectId(work_id)})
    flash("Work Successfully Deleted!")
    return redirect(url_for("works"))


# artists page
@app.route("/artists")
def artists():
    artists = mongo.db.artists.find().sort("artist_name", 1)
    crews = mongo.db.artists.find().sort("artist_crews", 1)
    return render_template("artists.html", artists=artists, crews=crews)


# get artist page
@app.route("/artist/<artist_name>")
def artist(artist_name):
    artist = mongo.db.artists.find_one({"artist_name": str(artist_name)})
    works = mongo.db.works.find({"artist_name": str(artist_name)})
    return render_template("artist.html", artist=artist, works=works)


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
        return redirect(url_for("artists"))

    crews = list(mongo.db.crews.find().sort("crew_name", 1))
    return render_template("add_artist.html", crews=crews)


# edit artist page
@app.route("/edit_artist/<artist_name>", methods=["GET", "POST"])
def edit_artist(artist_name):
    if request.method == "POST":
        update_artist = {
            "artist_name": request.form.get("artist_name")
        }
        mongo.db.artists.update_one({"artist_name": str(artist_name)}, {"$set": update_artist})
        flash("Artist Successfully Updated!")
        return redirect(url_for("artists"))

    artist = mongo.db.artists.find_one({"artist_name": str(artist_name)})
    return render_template("edit_artist.html", artist=artist)


# delete artist route
@app.route("/delete_artist/<artist_name>")
def delete_artist(artist_name):
    mongo.db.artists.remove({"artist_name": str(artist_name)})
    flash("Artist Successfully Deleted!")
    return redirect(url_for("artists"))


# crews page
@app.route("/crews")
def crews():
    crews = list(mongo.db.crews.find().sort("crew_name", 1))
    return render_template("crews.html", crews=crews)


# get crew page
@app.route("/crew/<crew_name>")
def crew(crew_name):
    crew = mongo.db.crews.find_one({"crew_name": str(crew_name)})
    artists = mongo.db.artists.find({"artist_crews": str(crew_name)})
    works = list(mongo.db.works.find().sort("artist_name", 1))
    return render_template("crew.html", crew=crew, artists=artists, works=works)


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
        return redirect(url_for("crews"))

    return render_template("add_crew.html")


# edit crew page
@app.route("/edit_crew/<crew_name>", methods=["GET", "POST"])
def edit_crew(crew_name):
    if request.method == "POST":
        update_crew = {
            "crew_name": request.form.get("crew_name"),
            "crew_image": request.form.get("crew_image"),
            "submitted_by": session["user"]
            }
        mongo.db.crews.update_one({"crew_name": str(crew_name)}, {"$set": update_crew})
        flash("Crew Successfully Updated!")
        return redirect(url_for("crews"))

    crew = mongo.db.crews.find_one({"crew_name": str(crew_name)})
    return render_template("edit_crew.html", crew=crew)


# delete crew route
@app.route("/delete_crew/<crew_name>")
def delete_crew(crew_name):
    mongo.db.crews.remove({"crew_name": str(crew_name)})
    flash("Crew Successfully Deleted!")
    return redirect(url_for("crews"))


# styles page
@app.route("/styles")
def styles():
    styles = list(mongo.db.styles.find().sort("style_type", 1))
    return render_template("styles.html", styles=styles)


# get style page
@app.route("/style/<style_type>")
def style(style_type):
    style = mongo.db.styles.find_one({"style_type": str(style_type)})
    works = mongo.db.works.find({"style_type": str(style_type)})
    return render_template("style.html", style=style, works=works)


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
            return redirect(url_for("styles"))

        return render_template("add_style.html")

    return redirect(url_for("styles"))


# edit style page
@app.route("/edit_style/<style_type>", methods=["GET", "POST"])
def edit_style(style_type):
    if session["user"] == "admin":
        if request.method == "POST":
            update_style = {
                "style_type": request.form.get("style_type")
            }
            mongo.db.styles.update_one({"style_type": str(style_type)}, {"$set": update_style})
            flash("Style Successfully Updated!")
            return redirect(url_for("styles"))

        style = mongo.db.styles.find_one({"style_type": str(style_type)})
        return render_template("edit_style.html", style=style)
    
    return redirect(url_for("styles"))


# delete style route
@app.route("/delete_style/<style_type>")
def delete_style(style_type):
    if session["user"] == "admin":
        mongo.db.styles.remove({"style_type": str(style_type)})
        flash("Style Successfully Deleted!")
        return redirect(url_for("styles"))

    return redirect(url_for("styles"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
