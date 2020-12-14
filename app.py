# import libraries & dependencies
import os
from dns.resolver import query
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# mongodb config vars
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# global variables
mongo = PyMongo(app)
all_works = list(mongo.db.works.find().sort("date_submitted", -1))


# pagination 
def get_works(offset=0, per_page=1):
    return all_works[offset: offset + per_page]


# routes
@app.route("/")
@app.route("/welcome")
def welcome():
    """welcome:
    
    * Displays welcome page template.
    
    \n Args: 
    *   None.
    
    \n Returns:  
    *  Template displaying index.html welcome page.
    """
    
    return render_template("index.html")


@app.route("/works")
def works():
    """works:
    
    * Displays every work upoaded to db.
    
    \n Args: 
    *   None.
    
    \n Returns:  
    *  Template displaying all works from db in date_submitted descending order.
    """
    
    page, per_page, offset = get_page_args(page_parameter='page',
                                            per_page_parameter='per_page')
    per_page = 15
    total = len(all_works)
    pagination_works = get_works(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template("works.html", works=pagination_works, page=page, per_page=per_page, pagination=pagination)


@app.route("/search", methods=["GET", "POST"])
def search():
    """search:
    
    * Takes user input from works page search box.
    * Queries db for results based on user input.
    
    \n Args: 
    1. query(str): user input from search box field.
    
    \n Returns:
    *   Template containing any results matching query input.
    *   h2 containing 'No Results Found' is returned if no results.
    """

    query = request.form.get("query")
    works = list(mongo.db.works.find({"$text": {"$search": query}}))
    return render_template("works.html", works=works)


@app.route("/filter/<filter_type>/<direction>")
def filter(filter_type, direction):
    """filter:
    
    * Checks for selected sort order
    * Sets the order in which the data will display on main page.
    * Displays data in defined order.
    
    \n Args:
    1.  filter_type(str): Targeted field within db collection.
    2.  direction(str): Direction of db sort order (ascending or descending).
    
    \n Returns: 
    *   Template displaying works from db in respective sort order.
    """

    if direction == 'ascending':
        works = list(mongo.db.works.find().sort(filter_type, 1))
        return render_template("works.html", works=works)

    works = list(mongo.db.works.find().sort(filter_type, -1))   
    return render_template("works.html", works=works)


@app.route("/work/<work_id>")
def work(work_id):
    """work:
    
    * Fetches selected work data from db collection.
    * Passes data to template for work page.
    
    \n Args:
    1.  work_id(str): ObjectId of selected work.
    
    \n Returns: 
    *   Template to diplay all content of individual object from collection.
    """

    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
    artists = mongo.db.artists.find()
    crews = mongo.db.crews.find()
    return render_template("work.html", work=work, artists=artists, crews=crews)


@app.route("/register", methods=["GET", "POST"])
def register():
    """register:
    
    * Searches db for existing user.
    * Appends new user data to db if not already existing.
    * Renders profile page for user account or register page.
    
    \n Args:
    1.  user inputs(str): username and password from form fields.
    
    \n Returns:
    *   User profile page on successful register. 
    *   Reloads register page with flash displaying error if unsucessful.
    """

    if request.method == "POST":
        # check db for existing username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(user)

        # insert user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """login:
    
    * Checks if user exists in db.
    * Logs user in if credentials match.
    * Appends username to session['user'] cookie.
    
    \n Args:
    *   User inputs(str): username and password from form fields.
    
    \n Returns:
    *   User profile template if successful.
    *   Login page with flash displaying error if unsuccessful.
    """

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


@app.route("/profile/<username>")
def profile(username):
    """profile:
    
    * Checks session cookies for 'user'.
    * Returns user profile template.
    * Shows all works and artists user has created in db.
    
    \n Args:
    1.  username(str): Users registered username.
    
    \n Returns:
    *   Template displaying associated user data.
    *   Login page if user does not exist.
    """

    if 'user' in session:
        # get session user's username from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        works = mongo.db.works.find({"submitted_by": username})
        artists = mongo.db.artists.find({"submitted_by": username})
        return render_template(
            "profile.html", username=username, works=works, artists=artists)
    
    return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    """logout:
    
    * Removes 'user' session cookie.
    * Returns to login page.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Removes 'user' session cookie.
    """

    flash("Sucessfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/new_work", methods=["GET", "POST"])
def new_work():
    """new_work:
    
    * Loads artist and style data from db to display in dropdown input fields.
    * Requests data from user input form fields when method is POST.
    * Appends data from requested fields to db.
    * Returns works template with flash displaying success.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Creates new work object in works db collection.
    """

    if 'user' in session:
        if request.method == "POST":
            work = {
                "artist_name": request.form.get("name"),
                "year_painted": request.form.get("year_painted"),
                "style_name": request.form.get("style_name"),
                "type_name": request.form.get("type_name"),
                "image_url": request.form.get("image_url"),
                "submitted_by": session["user"],
                "date_submitted": datetime.now()
                }
            mongo.db.works.insert_one(work)
            flash("Work Successfully Uploaded!")
            return redirect(url_for("works"))

        artists = mongo.db.artists.find().sort("artist_name", 1)
        crews = mongo.db.crews.find().sort("crew_name", 1)
        artiststyles = mongo.db.styles.find().sort("style_name", 1)
        crewstyles = mongo.db.styles.find().sort("style_name", 1)
        artisttypes = mongo.db.types.find().sort("type_name", 1)
        crewtypes = mongo.db.types.find().sort("type_name", 1)
        return render_template("new_work.html", artists=artists, crews=crews, 
            artiststyles=artiststyles, crewstyles=crewstyles, artisttypes=artisttypes, crewtypes=crewtypes)

    return redirect(url_for("login"))


@app.route("/edit_work/<work_id>", methods=["GET", "POST"])
def edit_work(work_id):
    """edit_work:
    
    * Loads existing work data from db.
    * Updates data for work in db when method is POST.
    
    \n Args:
    *   work_id(str): ObjectId of selected work.
    
    \n Returns:
    *   Updates selected object data in collection.
    """

    if 'user' in session:
        if request.method == "POST":
            update_work = {
                "artist_name": request.form.get("artist_name"),
                "year_painted": request.form.get("year_painted"),
                "style_name": request.form.get("style_name"),
                "image_url": request.form.get("image_url"),
                "submitted_by": session["user"],
                }
            mongo.db.works.update_one({"_id": ObjectId(work_id)}, {"$set": update_work})
            flash("Work Successfully Updated!")

        work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
        artists =  mongo.db.artists.find().sort("artist_name", 1)
        styles = mongo.db.styles.find().sort("style_name", 1)
        types = mongo.db.types.find().sort("type_name", 1)
        return render_template("edit_work.html", work=work, artists=artists, styles=styles, types=types)

    return redirect(url_for("login"))


@app.route("/delete_work/<work_id>")
def delete_work(work_id):
    """delete_work:
    
    * Removes work object from db collection.
    * Returns works main page with flash displaying success.
    
    \n Args:
    *   work_id(str): ObjectId of selected work.
    
    \n Returns:
    *   Removes object from db collection.
    """

    if 'user' in session:
        mongo.db.works.remove({"_id": ObjectId(work_id)})
        flash("Work Successfully Deleted!")
        return redirect(url_for("works"))


@app.route("/artists")
def artists():
    """artists:
    
    * Fetches all artist names from db.
    * Fetches all artist crews from db.
    * Displays all artists by name and associated crews.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Template displaying artist names and crews.
    """

    artists = mongo.db.artists.find().sort("artist_name", 1)
    return render_template("artists.html", artists=artists)


@app.route("/artist/<artist_name>")
def artist(artist_name):
    """artist:
    
    * Fetches selected artist data from db collection.
    * Fetches selected artists works from db collection.
    * Passes data to template for artist page.
    
    \n Args:
    1.  artist_name(str): name of selected artist in db collection.
    
    \n Returns: 
    *   Template to diplay all content of individual object from collection.
    """

    artist = mongo.db.artists.find_one({"artist_name": str(artist_name)})
    works = list(mongo.db.works.find({"artist_name": str(artist_name)}))
    return render_template("artist.html", artist=artist, works=works)


@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    """add_artist:
    
    * Loads crew data from db to display in dropdown input fields.
    * Requests data from user input form fields when method is POST.
    * Appends data from requested fields to db.
    * Returns artists template with flash displaying success.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Creates new artist object in artists db collection.
    """

    if 'user' in session:
        if request.method == "POST":
            artist = {
                "artist_name": request.form.get("artist_name").upper(),
                "artist_crews": request.form.getlist("artist_crews"),
                "submitted_by": session["user"]
                }
            mongo.db.artists.insert_one(artist)
            flash("Artist Successfully Added!")
            return redirect(url_for("artists"))

        crews = list(mongo.db.crews.find().sort("crew_name", 1))
        return render_template("add_artist.html", crews=crews)
    
    return redirect(url_for("login"))


@app.route("/edit_artist/<artist_name>", methods=["GET", "POST"])
def edit_artist(artist_name):
    """edit_artist:
    
    * Loads existing artist data from db.
    * Updates data for artist in db when method is POST.
    
    \n Args:
    *   artist_name(str): artist name of selected artist in db collection.
    
    \n Returns:
    *   Updates selected artist object data in collection.
    """

    if 'user' in session:
        if request.method == "POST":
            update_artist = {
                "artist_name": request.form.get("artist_name").upper(),
                "artist_crews": request.form.getlist("artist_crews"),
                "submitted_by": session["user"]
                }
            mongo.db.artists.update_one({"artist_name": str(artist_name)}, {"$set": update_artist})
            flash("Artist Successfully Updated!")
            return redirect(url_for("artists"))

        artist = mongo.db.artists.find_one({"artist_name": str(artist_name)})
        crews = mongo.db.crews.find().sort("crew_name", 1)
        return render_template("edit_artist.html", artist=artist, crews=crews)

    return redirect(url_for("login"))


@app.route("/delete_artist/<artist_name>")
def delete_artist(artist_name):
    """delete_artist:
    
    * Removes work object from db collection.
    * Returns works main page with flash displaying success.
    
    \n Args:
    *   artist_name(str): artist name of selected artist in db collection.
    
    \n Returns:
    *   Removes object from db collection.
    """

    if 'user' in session:
        mongo.db.artists.remove({"artist_name": str(artist_name)})
        flash("Artist Successfully Deleted!")
        return redirect(url_for("artists"))

    return redirect(url_for("login"))


@app.route("/crews")
def crews():
    """crews:
    
    * Fetches all crews from db.
    * Displays all crews by name and image.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Template displaying crew names and images.
    """

    crews = mongo.db.crews.find().sort("crew_name", 1)
    return render_template("crews.html", crews=crews)


@app.route("/crew/<crew_name>")
def crew(crew_name):
    """crew:
    
    * Fetches selected crew data from db collection.
    * Fetches selected artists associated to the crew from db collection.
    * Passes data to template for crew page.
    
    \n Args:
    1.  crew_name(str): name of selected crew in db collection.
    
    \n Returns: 
    *   Template to diplay all content of individual crew object from collection.
    """

    crew = mongo.db.crews.find_one({"crew_name": str(crew_name)})
    artists = mongo.db.artists.find({"artist_crews": str(crew_name)})
    works = mongo.db.works.find({"artist_name": str(crew_name)})
    return render_template("crew.html", crew=crew, artists=artists, works=works)


@app.route("/add_crew", methods=["GET", "POST"])
def add_crew():
    """add_crew:
    
    * Requests data from user input form fields when method is POST.
    * Appends data from requested fields to db.
    * Returns crews template with flash displaying success.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Creates new crew object in crews db collection.
    """

    if 'user' in session:
        if request.method == "POST":
            crew = {
                "crew_name": request.form.get("crew_name").upper(),
                "crew_image": request.form.get("crew_image"),
                "submitted_by": session["user"]
                }
            mongo.db.crews.insert_one(crew)
            flash("Crew Successfully Added!")
            return redirect(url_for("crews"))

        return render_template("add_crew.html")
    
    return redirect(url_for("login"))


@app.route("/edit_crew/<crew_name>", methods=["GET", "POST"])
def edit_crew(crew_name):
    """edit_crew:
    
    * Loads existing crew data from db.
    * Updates data for crew in db when method is POST.
    
    \n Args:
    *   crew_name(str): name of selected crew in db collection.
    
    \n Returns:
    *   Updates selected artist object data in collection.
    """

    if 'user' in session:
        if request.method == "POST":
            update_crew = {
                "crew_name": request.form.get("crew_name").upper(),
                "crew_image": request.form.get("crew_image"),
                "submitted_by": session["user"]
                }
            mongo.db.crews.update_one({"crew_name": str(crew_name)}, {"$set": update_crew})
            flash("Crew Successfully Updated!")
            return redirect(url_for("crews"))

        crew = mongo.db.crews.find_one({"crew_name": str(crew_name)})
        return render_template("edit_crew.html", crew=crew)
    
    return redirect(url_for("login"))


@app.route("/delete_crew/<crew_name>")
def delete_crew(crew_name):
    """delete_crew:
    
    * Removes crew object from db collection.
    * Returns crews page with flash displaying success.
    
    \n Args:
    *   crew_name(str): name of selected crew in db collection.
    
    \n Returns:
    *   Removes object from db collection.
    """

    if 'user' in session:
        mongo.db.crews.remove({"crew_name": str(crew_name)})
        flash("Crew Successfully Deleted!")
        return redirect(url_for("crews"))

    return redirect(url_for("login"))


@app.route("/styles")
def styles():
    """styles:
    
    * Fetches all style names from db.
    * Displays all styles by style name.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Template displaying style names in ascending order.
    """

    styles = mongo.db.styles.find().sort("style_name", 1)
    return render_template("styles.html", styles=styles)


@app.route("/style/<style_name>")
def style(style_name):
    """style:
    
    * Fetches selected style data from db collection.
    * Fetches works in selected style from db collection.
    * Passes data to template for style page.
    
    \n Args:
    1.  style_name(str): name of style in db collection.
    
    \n Returns: 
    *   Template to diplay all content of individual style object from collection.
    """

    style = mongo.db.styles.find_one({"style_name": str(style_name)})
    works = mongo.db.works.find({"style_name": str(style_name)})
    return render_template("style.html", style=style, works=works)


@app.route("/add_style", methods=["GET", "POST"])
def add_style():
    """add_style:
    
    * Requests data from user input form fields when method is POST.
    * Appends data from requested fields to db.
    * Returns styles template with flash displaying success.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Creates new style object in styles db collection.
    """

    if 'user' in session:
        if session["user"] == "admin":
            if request.method == "POST":
                style = {
                    "style_name": request.form.get("style_name"),
                    "style_image": request.form.get("image_url")
                    }
                mongo.db.styles.insert_one(style)
                flash("Style Successfully Added!")
                return redirect(url_for("styles"))

            return render_template("add_style.html")

        return redirect(url_for("styles"))
    
    return redirect(url_for("login"))


@app.route("/edit_style/<style_name>", methods=["GET", "POST"])
def edit_style(style_name):
    """edit_style:
    
    * Loads existing style data from db.
    * Updates data for style in db when method is POST.
    
    \n Args:
    *   style_name(str): name of style in db collection.
    
    \n Returns:
    *   Updates selected style object data in collection.
    """

    if 'user' in session:
        if session["user"] == "admin":
            if request.method == "POST":
                update_style = {
                    "style_name": request.form.get("style_name"),
                        "style_image": request.form.get("image_url")
                }
                mongo.db.styles.update_one({"style_name": str(style_name)}, {"$set": update_style})
                flash("Style Successfully Updated!")
                return redirect(url_for("styles"))

            style = mongo.db.styles.find_one({"style_name": str(style_name)})
            return render_template("edit_style.html", style=style)
        
        return redirect(url_for("styles"))
    
    return redirect(url_for("login"))


@app.route("/delete_style/<style_name>")
def delete_style(style_name):
    """delete_style:
    
    * Removes style object from db collection.
    * Returns styles page with flash displaying success.
    
    \n Args:
    *   style_name(str): name of style in db collection.
    
    \n Returns:
    *   Removes object from db collection.
    """

    if 'user' in session:
        if session["user"] == "admin":
            mongo.db.styles.remove({"style_name": str(style_name)})
            flash("Style Successfully Deleted!")
            return redirect(url_for("styles"))

        return redirect(url_for("styles"))
    
    return redirect(url_for("login"))


@app.route("/types")
def types():
    """types:
    
    * Fetches all type names from db.
    * Displays all types by type name.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Template displaying types in name ascending order.
    """

    types = mongo.db.types.find().sort("type_name", 1)
    return render_template("types.html", types=types)


@app.route("/type/<type_name>")
def type(type_name):
    """type:
    
    * Fetches selected type data from db collection.
    * Fetches works of selected type from db collection.
    * Passes data to template for type page.
    
    \n Args:
    1.  type_name(str): name of type in db collection.
    
    \n Returns: 
    *   Template to diplay all content of individual type object from collection.
    """

    type = mongo.db.types.find_one({"type_name": str(type_name)})
    works = mongo.db.works.find({"type_name": str(type_name)})
    return render_template("type.html", type=type, works=works)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    """add_type:
    
    * Checks for admin user authentication.
    * Requests data from user input form fields when method is POST.
    * Appends data from requested fields to db.
    * Returns types template with flash displaying success.
    
    \n Args:
    *   None.
    
    \n Returns:
    *   Creates new type object in types db collection.
    """

    if 'user' in session:
        if session["user"] == "admin":
            if request.method == "POST":
                style = {
                    "type_name": request.form.get("type_name"),
                    "type_image": request.form.get("image_url")
                    }
                mongo.db.types.insert_one(style)
                flash("Style Successfully Added!")
                return redirect(url_for("types"))

            return render_template("add_type.html")

        return redirect(url_for("types"))
    
    return redirect(url_for("login"))


@app.route("/edit_type/<type_name>", methods=["GET", "POST"])
def edit_type(type_name):
    """edit_type:
    
    * Checks for admin user authentication.
    * Loads existing type data from db.
    * Updates data for type in db when method is POST.

    \n Args: 
    1.  type_name(str): name of type in db collection.
    
    \n Returns:
    *   Updates selected style object data in collection.
    """

    if 'user' in session:
        if session["user"] == "admin":
            if request.method == "POST":
                update_type = {
                    "type_name": request.form.get("type_name"),
                    "type_image": request.form.get("image_url")
                }
                mongo.db.types.update_one({"type_name": str(type_name)}, {"$set": update_type})
                flash("Type Successfully Updated!")
                return redirect(url_for("types"))

            type = mongo.db.types.find_one({"type_name": str(type_name)})
            return render_template("edit_type.html", type=type)
        
        return redirect(url_for("types"))
    
    return redirect(url_for("login"))


@app.route("/delete_type/<type_name>")
def delete_type(type_name):
    """delete_type:
    
    * Checks for admin user authentication.
    * Removes type object from db.
    * Returns types page template.
    
    \n Args: 
    1.  type_name(str): name of type in db collection.
    
    \n Returns:
    *  Removes type object from db.
    """

    if 'user' in session:
        if session["user"] == "admin":
            mongo.db.types.remove({"type_name": str(type_name)})
            flash("type Successfully Deleted!")
            return redirect(url_for("types"))

        return redirect(url_for("types"))
    
    return redirect(url_for("login"))


@app.route("/admin_panel")
def admin_panel():
    """admin_panel:
    
    * Checks for admin user authentication.
    * Displays admin panel page.
    * Redirects non admin users to home page.
    
    \n Args: 
    1.  None.
    
    \n Returns:
    *  Template displaying admin panel page if user is admin.
    """

    if 'user' in session:
        if session["user"] == "admin":
            users = list(mongo.db.users.find().sort("username", 1))
            return render_template("admin-panel.html", users=users)

        return redirect(url_for("works"))
    
    return redirect(url_for("login"))


@app.route("/delete_user/<username>")
def delete_user(username):
    """delete_user:
    
    * Checks for admin user authentication.
    * Removes user object from db.
    * Displays admin panel for admin user.
    * Displays Works page for non admin user.
    
    \n Args: 
    1.  username(str): name of user in db collection.
    
    \n Returns:  
    *  Removes user object from db.
    """

    if 'user' in session:
        if session["user"] == "admin":
            mongo.db.users.remove({"username": str(username)})
            flash("User Deleted!")
            return redirect(url_for("admin_panel"))

        mongo.db.users.remove({"username": str(username)})
        session.pop("user")
        flash("User Deleted!")
        return redirect(url_for("works"))
    
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    """page_not_found:
    
    * Displays error handling page.
    
    \n Args: 
    *   Error event code.
    
    \n Returns:
    *  Template displaying error handling page.
    """

    return render_template('404.html'), 404


# Environment Variables
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))