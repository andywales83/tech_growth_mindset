# **Tech Growth Mindset**

Tech Growth Mindset is a Web-based Application, specifically built for the Data-Centric Development modules of the Code Institute's - Full Stack Software Development Diploma. The purpose of the project, is to give users access to sharable information and resources, around Technology and Self Development, through a number of different platforms. The Application is built, following the "CRUD" principles and will allow users to Create, Read, Update and Delete content. 

[View the live project on Heroku](#)

![Am I responsive image](#)

---
## **Contents**

- [UX Design](#ux-design)
- [UI Design](#ux-design)
- [Wireframes](#wireframes)
- [Data Structure](#data-structure) 
- [Existing Features](#existing-features)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## **UX Design**


### **User Goals**

- Be able to post, edit or delete, own content.
- Be able to view posted content of other site users.
- Be able to save relevant content for future reference.
- Be able to use the application on Mobile, Tablet or Desktop devices. 


### **Site Owners Goals**

- Provide a positive experience for all users, looking to access the application.
- To create a space for all users, to find insightful Tech and Self-Development resources, that meets their needs, whilst maintaining the positive overall experience.

### **User Requirements and Expectations**
#### Requirements 

- Easily identifiable navigation
- Clean and structured layout
- Visually appealing elements
- Access to insightful resources that promote a positive experience

#### Expectations

- When using the main navigational links, the user should be directed to each part of the application without issue.
- Links clicked on in the user resources, should open in a new page and not overwrite the current page that the user is on.
- The ability to Create, Read, Update and Delete resources, as set down in the sites overall purpose.
- Notifications that tell the user when they have carried out a relevant activity.

### **User Stories**

#### *New Visitor*
1. As a first time visitor, I want the main purpose of the site to be immediately clear.
2. As a first time visitor, I want the look of the site to be visually appealing.
3. As a first time visitor, I want the layout of the site to be well structured and easy to navigate.
4. As a first time visitor, I want to have an idea of the content that the site offers, before deciding to register.
5. As a first time visitor, I want to see ways of communicating with the site's creators, via social media or a contact page.

#### *Registered User*
1. As a registered user, I want to be able to login with a set of registered credentials.
2. As a registered user, I want to be able to change my user credentials.
3. As a registered user, I want to be able to see all resources posted by other members.
4. As a registered user, I want to be able to edit or delete posts that I have created myself.
5. As a registered user, I want to be able to see a profile page where I can review my saved resource posts.
6. As a registered user, I want to be able to quickly serach for relevant resources.
7. As a registered user, I want to be able to delete my account in full, if i no longer wish to remain a member.

#### *Site Administrator*
1. As a site Administrator, I would want to be able to control the main functionality of the site, including adding new categories and topics.
2. As a site Administrator, I would want to be able to edit or delete categories and topics.
3. As a site Administrator, I would want to be able to control the resources added and select weekly featured resources.
4. As a site Administrator, I would want to be able to view all resource posts added by users and delete where necessary, keeping the site up-to date.
5. As a site Administrator, I would want to be able to add new users or delete users who have issues with functionality.

---

## **UI Design**

---

## **Wireframes**

---

## **Data Structures**

---

## **Existing Features**

---

## **Future Features**

---

## **Technologies Used**

### Development Languages
- The project is built using the HTML, CSS, Javascript and Python programming languages.

### Development Tools
- [GitHub](https://github.com/)
    - The cloud based repository platform, used to hold the programme files and documents upon which the application depends.

- [Gitpod](https://www.gitpod.io/)
    - The Intergrated Development Environment used to work on the programming files.

- [Heroku](https://id.heroku.com/login)
    - A cloud based platform allowing developers to build, run and operate applications.

- [MongoDB](https://www.mongodb.com/)
    - Cloud based database platform, used to hold data for applications.

### Libraries, Frameworks and Dependencies


### Design Tools

- [Balsamiq](https://balsamiq.com/)
    - Cloud or application based wireframing software, used for building low fidelity mockups. 
---

## **Testing**

---

## **Deployment**
The project uses GitHub for version control, Gitpod as the development platform and Heroku for final production deployment.

### **Cloning the project through GitHub:**
- To clone the project from the GitHub repository, visit https://github.com/andywales83/tech_growth_mindset
- Above the central file container of the repository, click the "Code" button.
- Save the downloaded repository file to your machine and open the folder with your chosen development platform.

Alternatively, you can clone the repository directly through your terminal, using:
```
git clone https://github.com/andywales83/tech_growth_mindset
```

In order to run work with the application, you will need to have the following technologies installed in your working environment:

- [PIP3](https://pip.pypa.io/en/stable/installation/)
- [Python3](https://www.python.org/downloads/)

### **Setting Up MongoDB Atlas for Database Usage**
The project uses MongoDB for its backend database functionality. If you wish to create your own database of information to use with this project, you will need to create an account with MongoDB Atlas. Details on how to do this, can be found here: [MongoDB Atlas](https://docs.atlas.mongodb.com/).

When setting up the database, the following setps are required:

1. Start by creating a Cluster (this will be the service that the database will run on).
2. Add and authenticate a new database user.
3. Once the cluster has been created, click the 'Browse Collections' button.
4. Click '+ Create Database'.
5. Click on the 'Create Collection' button.
6. Create the data collections that you want in the database.
7. Click on 'Insert Document'.
8. Add the neccessary key: value pairs, to be collected in each collection.

### **Flask Development Setup**

In oredr to build the application, the following steps are to be taken:

1. Firstly you need to install Flask. In your terminal, type:
```
pip3 install flask
```

2. Next is to create a few new files. First will be a Python file, that will be the foundation of the application. Your can call your file anything, but in this instance, I will call the file `app.py`:
```
touch app.py
``` 

3. Next we create a file called `env.py`, in which to store sensitive data using environment variables, so type:
```
touch env.py
```

4. Our `env.py` file should never be pushed to GitHunb and needs to be ignored. To do this first create a `gitignore`file by typing:
```
touch .gitignore
```

5. Within the gitignore file, add the `env.py` file and `__pycache__/` directory, which will be auto-generated shortly. 

6. Now we need to add several bits of data to the `env.py` file. Open the file and add the following:
```
import os

os.environ["IP"] = "0.0.0.0"
os.environ["PORT"] = "5000"
os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
os.environ["MONGO_DBNAME"]= "DATABASE_NAME"
```

7. Next we need to add some data to the `app.py`file. Open the file and add the following:
```
import os

from flask import (
Flask, flash, render_template,
redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
```

8. Now we can create an instance of Flask, that will be stored in a variable called 'app'.
```
app = Flask(__name__)
```

9. Finally, we can test the application. To do this, we need tell our app how and where to run the application. Set up your 'IP' and 'PORT' environment variables in the hidden `env.py` file. Make sure to udate the `debug=True` varieable to `debug=False` before final deployment.
```
if __name__ == "__main__":
app.run(host=os.environ.get("IP"),
port=int(os.environ.get("PORT")),
debug=True)
```

10. You can now run your application from the command line using:
```
python3 app.py
```

### **Deploy the application to Heroku**

1. Before you create your Heroku application, you need to setup some files that Heroku needs
to run the app.

2. First, you need to tell Heroku which applications and dependencies are required to run our app. In the terminal, type:
```
pip3 freeze --local > requirements.txt
```

3. Next is the Procfile. This is what Heroku looks for to know which file runs the app, and how to
run it. In the terminal, type:
```
echo web: python app.py
```
- The Procfile might add a blank line at the bottom, and sometimes this can cause problems, when running our app on Heroku, so just delete that line and save the file.

4. Now head to [Heroku.com](https://id.heroku.com/login) and create an account. When you are logged in, click on the button labeled "New" and select "Create new app".

5. Give your app a name and select a local location.

6. On the Heroku dashbord from within your app, click on the 'GitHub - Connect to GitHub' button and serach for the name of the GitHub relevant repository. Then click 'Connect'.

7. When the repository is showing as connected, and before selecting 'Enable Automatic Deploys', click on the settings tab for the app, and then click on 'Reveal Config Vars'. Here you will tell Heroku, which variables are required. These will be the key:value environment variables, from the `env.py` file:
```
["IP"] = "0.0.0.0"
["PORT"] = "5000"
["SECRET_KEY"] = "YOUR_SECRET_KEY"
["MONGO_URI"] = "YOUR_MONGODB_URI"
["MONGO_DBNAME"]= "DATABASE_NAME"
``` 

8. Next, commit the `requirements.txt` and `procfile` to GitHub, to ensure all files are available on the repository.

9. Finally, head back to Heroku and click on the 'Enable Automatic Deploys' button. Heroku will now start building the application from the GitHub repository.

10. Once the application has been built, click on the 'Open App' button on the dashboard.
---



## Credits