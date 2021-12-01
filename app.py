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


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# create the link to PyMongo
mongo = PyMongo(app)


# ----------------------------------------------- #
# Registration and Log In / Log Out Functionality #
# ----------------------------------------------- #

# --- Sign Up / Register Functionality ---#
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    User registration - this functionality will take user submitted details,
    and check them against the database to see if they already exist. If they
    already exist, the user will be shown a message telling them that the
    details exist and they are redirected back to the page. If the details do
    not exist, the details are submitted to the database and a success message
    is shown.
    """
    if request.method == "POST":
        # check if the username is already registered on the database.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if the username exists in the database, alert user
        if existing_user:
            flash("Ooops! Its looks like this username already exists.")
            # redirect the user back to the sign up page.
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Congratulations! You are now signed up.")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# ----- Log In Functionality ----- #
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    User Log In - this functionality checks if the users details
    that are input, are registered against the database already.
    If the details match, the user is logged in. If the details do
    not match, the user is sent back to the Log In page.
    """
    if request.method == "POST":
        # Check username against database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if details exist - check passwords match
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Your Username and/or Password are incorrect")
                return redirect(url_for("login"))

        else:
            # if the username doesn't exist show message
            flash("Your Username and/or Password are incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


# ----- Log Out Functionality ----- #
@app.route("/logout")
def logout():
    # remove user session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# --------------------------- #
# Resource CRUD Functionality #
# --------------------------- #

# ----- Create a resource functionality ----- #
@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    if request.method == "POST":
        form_data = {
            "resource_name": request.form.get("resource_name"),
            "category_name": request.form.get("category_name"),
            "resource_topic": request.form.get("resource_topic"),
            "date_added": request.form.get("date_added"),
            "resource_description": request.form.get("resource_description"),
            "resource_link": request.form.get("resource_link"),
            "created_by": session["user"]
        }
        mongo.db.resources.insert_one(form_data)
        flash("Awesome! Your resource has been added.")
        return redirect(url_for("add_resource"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("add_resource.html", categories=categories,
                           topics=topics)


# ----- Edit Resource Functionality ----- #
@app.route("/edit_resource/<resource_id>", methods=["POST", "GET"])
def edit_resource(resource_id):
    if request.method == "POST":
        edit_data = {
            "resource_name": request.form.get("resource_name"),
            "category_name": request.form.get("category_name"),
            "resource_topic": request.form.get("resource_topic"),
            "date_added": request.form.get("date_added"),
            "resource_description": request.form.get("resource_description"),
            "resource_link": request.form.get("resource_link"),
            "created_by": session["user"]
        }
        mongo.db.resources.update({"_id": ObjectId(resource_id)}, edit_data)
        flash("Your resource has been updated.")
        return redirect(url_for("get_resources"))

    resource = mongo.db.resources.find_one({"_id": ObjectId(resource_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("edit_resource.html", resource=resource,
                           categories=categories, topics=topics)


# ---------- Profile Functionality ---------- #
@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    # retrieve the name of the session user from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_resources")
def get_resources():
    resources = list(mongo.db.resources.find())
    return render_template("resources.html", resources=resources)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
