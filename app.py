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
    return render_template("register.html", page_title="Register")


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

    return render_template("login.html", page_title="Login")


# ---------- Log Out Functionality ---------- #
@app.route("/logout")
def logout():
    """
    Log Out - This function logs the user out of the site and removes
    them from the session. The user will see a message telling them they
    have been logged out, as they are redirected to the login page.
    """
    # remove user session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------------------------------------ #
# Resource CRUD Functionality & Search #
# ------------------------------------ #

# ---------- Create Resource Functionality ---------- #
@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    """
    Add Resource. This function first checks if the user is in session.
    When user is in session and submits a new request, find the resources
    in the database and add the new items to the database. If this was
    successful, the user is notified and returned to the resources page.
    """
    if "user" not in session:
        flash("You must be logged in to view this page.")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            form_data = {
                "resource_name": request.form.get("resource_name"),
                "category_name": request.form.get("category_name"),
                "resource_topic": request.form.get("resource_topic"),
                "date_added": request.form.get("date_added"),
                "resource_description": request.form.get(
                    "resource_description"),
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
                           topics=topics, page_title="Add Resource")


# ---------- Read Resource Functionality ---------- #
@app.route("/get_resources/")
def get_resources():
    """
    Get resources function. This function first checks if the
    user is in session. If the user is not in session, they are
    redirected to the login page. If user in session, it will find
    all of the resources in the database and list them on the resources page.
    """
    if "user" not in session:
        flash("You must be logged in to view this page.")
        return redirect(url_for("login"))
    else:
        resources = list(mongo.db.resources.find())

    return render_template("resources.html", resources=resources,
                           page_title="Resources")


# ---------- Edit Resource Functionality ---------- #
@app.route("/edit_resource/<resource_id>", methods=["POST", "GET"])
def edit_resource(resource_id):
    """
    Edit Resource function. This first checks the database for the
    resource and returns a 404 if not found. The functionality also
    checks if the user is in session and redircets them to the login
    page if not. If user in session and data can be found, edit page
    is shown with data pre-populated
    """
    resource = mongo.db.resources.find_one_or_404(
        {"_id": ObjectId(resource_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    topics = mongo.db.topics.find().sort("topic_name", 1)

    if "user" not in session:
        flash("You must be logged in to view this page.")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            weekly_featured = "on" if request.form.get(
                "weekly_featured") else "off"

            edit_data = {
                "resource_name": request.form.get("resource_name"),
                "category_name": request.form.get("category_name"),
                "resource_topic": request.form.get("resource_topic"),
                "date_added": request.form.get("date_added"),
                "resource_description": request.form.get(
                    "resource_description"),
                "resource_link": request.form.get("resource_link"),
                "created_by": session["user"],
                "weekly_featured": weekly_featured
            }
            mongo.db.resources.update({"_id": ObjectId(resource_id)},
                                      edit_data)
            flash("Your resource has been updated.")
            return redirect(url_for("get_resources"))

    return render_template("edit_resource.html", resource=resource,
                           categories=categories, topics=topics,
                           page_title="Edit Resource")


# ---------- Delete Resource Functionality ---------- #
@app.route("/delete_resource/<resource_id>")
def delete_resource(resource_id):
    """
    Delete Resource function. Using the specific ObjectId, the
    resource is deleted from the database. The user receives a
    confirmation message and is redirected back to the resources
    page.
    """
    mongo.db.resources.remove({"_id": ObjectId(resource_id)})
    flash("Your resource has been deleted!")
    return redirect(url_for("get_resources"))


# ---------- Saerch Functionality ----------- #
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search Functionality. To query the resources in the database
    and find the resources that match the query.
    """
    query = request.form.get("query")
    resources = list(mongo.db.resources.find({"$text": {"$search": query}}))
    return render_template("resources.html", resources=resources,
                           page_title="Resources")


# --------------------------- #
# Administrator Functionality #
# --------------------------- #

# ---------- Link to Admin Page ---------- #
@app.route("/admin_dashboard")
def admin_dashboard():
    """
    Display Admin Dashboard. This page is restricted to the admin user.
    """
    if admin():
        return render_template("admin_dashboard.html",
                               page_title="Admin Dashboard")
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))


# ---------- Categories Functionality ---------- #

# ---------- Add New Category ---------- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Add Category. If the function is called using the POST method, then
    the data from the form is retrieved, and inserted into the database.
    Otherwise it will display the empty form.
    """
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

    return render_template("add_category.html", page_title="Add A Category")


# ---------- Get Categories From DB ---------- #
@app.route("/get_categories")
def get_categories():
    """
    Get Categories function. This function can be used by admin only and
    forms part of the content management basis of the site. This will list the
    current categories on the site in the manage categories section.
    """
    if admin():
        categories = list(mongo.db.categories.find().sort("category_name", 1))
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))

    return render_template("categories.html", categories=categories,
                           page_title="Categories")


# ---------- Edit Category ---------- #
@app.route("/edit_category/<category_id>", methods=["POST", "GET"])
def edit_category(category_id):
    """
    Edit Category Functionality. If the admin user submits an edit request,
    then the Category is retrieved from the database, updated in the database
    and after the user receives a message, they are taken back to the manage
    page.
    """    
    if admin():
        if request.method == "POST":
            submit = {
                "category_name": request.form.get("category_name")
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("The category was updated")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one_or_404(
            {"_id": ObjectId(category_id)})
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))
    
    return render_template("edit_category.html", category=category,
                           page_title="Edit Category")


# ---------- Delete Category ---------- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Delete Category Functionality. If the admin user wants to delete a
    category, then using the remove() method, it is deleted in the
    database. Thereafter, the user receives a message and they are
    taken back to the manage page.
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("The category was deleted")

    return redirect(url_for("get_categories"))


# ---------- Topics Functionality ---------- #

# ---------- Add New Topic ---------- #
@app.route("/add_topic", methods=["GET", "POST"])
def add_topic():
    """
    Add Topic. If the function is called using the POST method, then
    the data from the form is retrieved, and inserted into the database.
    Otherwise it will display the empty form.
    """
    if admin():
        if request.method == "POST":
            topic = {
                "topic_name": request.form.get("topic_name")
            }
            mongo.db.topics.insert_one(topic)
            flash("Your new topic was added!")
            return redirect(url_for("admin_dashboard"))
    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))

    return render_template("add_topic.html", page_title="Add A Topic")


# ---------- Get Topics From DB ----------#
@app.route("/get_topics")
def get_topics():
    """
    Get Topics function. This function can be used by admin only and
    forms part of the content management basis of the site. This will list the
    current Topics on the site in the manage topicss section.
    """
    topics = list(mongo.db.topics.find().sort("topic_name", 1))
    return render_template("topics.html", topics=topics,
                           page_title="Topics")


# ---------- Edit Topic ---------- #
@app.route("/edit_topic/<topic_id>", methods=["POST", "GET"])
def edit_topic(topic_id):
    """
    Edit Topic Functionality. If the user submits an edit request, then
    the topic is retrieved from the database, updated in the database and
    after the user receives a message, they are taken back to the manage page.
    """
    if admin():
        if request.method == "POST":
            topic = mongo.db.topics.find_one_or_404(
                {"_id": ObjectId(topic_id)})
            submit = {
                "topic_name": request.form.get("topic_name")
            }
            mongo.db.topics.update({"_id": ObjectId(topic_id)}, submit)
            flash("The topic was updated")
            return redirect(url_for("get_categories"))

    else:
        flash("You must be the Admin to view this page.")
        return redirect(url_for("login"))

    return render_template("edit_topic.html", topic=topic,
                           page_title="Edit Topics")


# ---------- Delete Topic ---------- #
@app.route("/delete_topic/<topic_id>")
def delete_topic(topic_id):
    """
    Delete Topic Functionality. If the admin user wants to delete a topic,
    then using the remove() method, it is deleted in the database. Thereafter,
    the user receives a message and they are taken back to the manage
    page.
    """
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

    # if the user is in session, render the profile template in their name
    if session["user"]:
        return render_template("profile.html", username=username,
                               resources=resources, page_title="Profile")

    return redirect(url_for("login"))


@app.route("/change_email/<username>", methods=["POST", "GET"])
def change_email(username):
    """
    Change Email Functionality where the user can change their current
    password on their profile page.
    """
    if request.method == "POST":
        new_email = request.form.get("email").lower()
        mongo.db.users.update(
            {"username": username},
            {"$set": {"email": new_email}})
        flash("Your email has been updated")
        return redirect(url_for("profile", username=session["user"]))


@app.route("/change_password/<username>", methods=["POST", "GET"])
def change_password(username):
    """
    Change Password Functionality where the user can change their current
    password on their profile page.
    """
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
    """
    Delete Profile Functionality where the user can delete their account
    on their profile page.
    """
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
    """
    Renders a custom 404 error page with a button
    that takes the user back to the home page.
    """
    return render_template("errors/404.html", page_title="404"), 404


# --- 500 Handler --- #
@app.errorhandler(500)
def internal_server_error(e):
    """
    Renders a custom 500 error page with a button
    that takes the user back to the home page.
    """
    return render_template("errors/500.html", page_title="500"), 500


@app.route("/")
@app.route("/index/")
def index():
    """Renders the template for the home page"""
    resources = list(mongo.db.resources.find(
        {"weekly_featured": "on"}))
    return render_template("index.html", resources=resources,
                           page_title="Home")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
