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


# ---------- Create Admin Function ---------- #
def admin():
    """
    Define admin user.
    """
    return session["user"] == "admin"


# ----------------------------------------------- #
# Registration and Log In / Log Out Functionality #
# ----------------------------------------------- #

# ---------- Sign Up / Register Functionality ----------#
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


# ---------- Log In Functionality ---------- #
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


# ---------- Log Out Functionality ---------- #
@app.route("/logout")
def logout():
    # remove user session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# --------------------------- #
# Resource CRUD Functionality #
# --------------------------- #

# ---------- Create Resource Functionality ---------- #
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
            "created_by": session["user"],
            "weekly_featured": request.form.get("weekly_featured")
        }
        mongo.db.resources.insert_one(form_data)
        flash("Awesome! Your resource has been added.")
        return redirect(url_for("get_resources"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("add_resource.html", categories=categories,
                           topics=topics)


# ---------- Read Resource Functionality ---------- #
@app.route("/get_resources/")
def get_resources():
    resources = list(mongo.db.resources.find())
    return render_template("resources.html", resources=resources)


# ---------- Edit Resource Functionality ---------- #
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
            "created_by": session["user"],
            "weekly_featured": request.form.get("weekly_featured")
        }
        mongo.db.resources.update({"_id": ObjectId(resource_id)}, edit_data)
        flash("Your resource has been updated.")
        return redirect(url_for("get_resources"))

    resource = mongo.db.resources.find_one({"_id": ObjectId(resource_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("edit_resource.html", resource=resource,
                           categories=categories, topics=topics)


# ---------- Delete Resource Functionality ---------- #
@app.route("/delete_resource/<resource_id>")
def delete_resource(resource_id):
    mongo.db.resources.remove({"_id": ObjectId(resource_id)})
    flash("Your resource has been deleted!")
    return redirect(url_for("get_resources"))


# --------------------------- #
# Administrator Functionality #
# --------------------------- #

# ---------- Link to Admin Page ---------- #
@app.route("/admin_dashboard")
def admin_dashboard():
    if admin():
        return render_template("admin_dashboard.html")
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))


# ---------- Categories Functionality ---------- #

# ---------- Add New Category ---------- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if admin():
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.insert_one(category)
            flash("Your new category was added!")
            return redirect(url_for("admin_dashboard"))
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))

    return render_template("add_category.html")


# ---------- Get Categories From DB ---------- #
@app.route("/get_categories")
def get_categories():
    if admin():
        categories = list(mongo.db.categories.find().sort("category_name", 1))
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))

    return render_template("categories.html", categories=categories)


# ---------- Edit Category ---------- #
@app.route("/edit_category/<category_id>", methods=["POST", "GET"])
def edit_category(category_id):
    if admin():
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("The category was updated")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))
    return render_template("edit_category.html", category=category)


# ---------- Delete Category ---------- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if admin():
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("The category was deleted")
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))
    return redirect(url_for("get_categories"))


# ---------- Topics Functionality ---------- #

# ---------- Add New Topic ---------- #
@app.route("/add_topic", methods=["GET", "POST"])
def add_topic():
    if request.method == "POST":
        topic = {
            "topic_name": request.form.get("topic_name")
        }
        mongo.db.topics.insert_one(topic)
        flash("Your new topic was added!")
        return redirect(url_for("admin_dashboard"))

    return render_template("add_topic.html")


# ---------- Get Topics From DB ----------#
@app.route("/get_topics")
def get_topics():
    topics = list(mongo.db.topics.find().sort("topic_name", 1))
    return render_template("topics.html", topics=topics)


# ---------- Edit Topic ---------- #
@app.route("/edit_topic/<topic_id>", methods=["POST", "GET"])
def edit_topic(topic_id):
    if request.method == "POST":
        submit = {
            "topic_name": request.form.get("topic_name")
        }
        mongo.db.topics.update({"_id": ObjectId(topic_id)}, submit)
        flash("The topic was updated")
        return redirect(url_for("get_categories"))

    topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
    return render_template("edit_topic.html", topic=topic)


# ---------- Delete Topic ---------- #
@app.route("/delete_topic/<topic_id>")
def delete_topic(topic_id):
    mongo.db.topics.remove({"_id": ObjectId(topic_id)})
    flash("The topic was deleted")
    return redirect(url_for("get_topics"))


# ---------- Profile Functionality ---------- #
@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    # retrieve the name of the session user from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    resources = list(mongo.db.resources.find(
        {"created_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, resources=resources)

    return redirect(url_for("login"))


@app.route("/change_email/<username>", methods=["POST", "GET"])
def change_email(username):
    if request.method == "POST":
        new_email = request.form.get("email").lower()
        mongo.db.users.update(
            {"username": username},
            {"$set": {"email": new_email}})
        flash("Your email has been updated")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/change_password/<username>", methods=["POST", "GET"])
def change_password(username):
    if request.method == "POST":
        new_password = generate_password_hash(request.form.get
                                              ("new_password"))
        mongo.db.users.update(
            {"username": username},
            {"$set": {"password": new_password}})
        flash("Your Password has been changed")
        return redirect(url_for("profile", username=session["user"]))


# --- Delete Profile Functionality --- #
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    user = mongo.db.users.find_one({'username': session["user"]})
    # Checks if password matches existing password in database
    if check_password_hash(user["password"],
                           request.form.get("confirm_deletion")):
        flash("We can confirm that your account has been deleted.")
        session.pop("user")
        mongo.db.users.remove({"_id": ObjectId(user['_id'])})
        return redirect(url_for("register"))
    else:
        flash("The password you entered was incorrect. Please try again!")
        return redirect(url_for("profile", username=session["user"]))
    # return to home page page
    return redirect(url_for("register"))


# ---------- Error Handling Functionality ---------- #

# --- 404 Handler --- #
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


# --- 500 Handler --- #
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500


@app.route("/")
@app.route("/index/")
def index():
    resources = list(mongo.db.resources.find(
        {"weekly_featured": "on"}))
    return render_template("index.html", resources=resources)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    resources = list(mongo.db.resources.find({"$text": {"$search": query}}))
    return render_template("resources.html", resources=resources)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
