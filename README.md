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
- Be able to view own posts in the profile page.
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
5. As a registered user, I want to be able to see a profile page where I can review my own resource posts.
6. As a registered user, I want to be able to quickly serach for relevant resources.
7. As a registered user, I want to be able to delete my account in full, if I no longer wish to remain a member.

#### *Site Administrator*
1. As a site Administrator, I would want to be able to control the main functionality of the site, including adding new categories and topics.
2. As a site Administrator, I would want to be able to edit or delete categories and topics.
3. As a site Administrator, I would want to be able to control the resources added and select weekly featured resources.
4. As a site Administrator, I would want to be able to view all resource posts added by users and delete where necessary, keeping the site up-to date.
5. As a site Administrator, I would want to be able to add new users or delete users who have issues with functionality.

---

## **UI Design**

### Fonts
- The project uses Google Fonts for the delivery of the main font styling.
- The main font used is the Rubik font, due to its clean and modern style.
- The back-up font used for the project is Sans-Serif.

### Colour Scheme
- The colour scheme was chosen to make the site look visually appealing, using a mix of bold and modern colours.
- The text for the site uses a generic dark grey colour.
- The background for the site uses the colour of "Honeydew".
- The resource cards use the "Powdered Blue" colour.
- The Navbar and Footer both use the "Celadon Blue" colour.

#### **Colour Palette**

 The overall colour palette was designed from a website called [Coolors](https://coolors.co/) and was selected, becasue of the broad spectrum of colour options available. However, not all colours in the palette are used. 
![Colour Palette](/documentation/images/general-images/milestone3-colour-palette-copy.png)

- #001219: The Rich Black color was used for the general font color of the site, so that it stands out against the differen backgroun colours.
- #005F73: The Blue Sapphire colour is used for the bacground colour of the navigation bar and for the footer   
- #94D2BD: The Middle Blue Green colour has been used as the background colour for all card based content.
- #F3EACE: The Cornsilk colour is used as the primary background colour for the whole site.
- #FD850D: The Orange colour has been used for the buttons that have an edit, submit or update function. The colour has been accented to a darker colour for the hover over feature.   
- #DE2817: The Vermillion colour has been used for the cancel and delete buttons, along with the modal trigger buttons. The colour has been accented to a darker colour for the hover over feature


### Icons
- Many of the icons used, were those provided by the Materialize Icons library. Where the Materialize library did not offer the required icon/s, Font Awesome was used as a substitute. 

---

## **Wireframes**

### **Low Fidelity Wireframes**

Low fidelity wireframes were created with Balsamiq, and bring to life the basic prototyping structure of how the site may initially be designed to look. 

---

## **Data Structures**
 - [MongoDB](https://www.mongodb.com/) is the cloud based storage application, hosting storeage of the data for Tech Growth Mindset. It is a non-relational database, used as the backend functionality of the application, that allows users to create, read, update, delete and search data records on the app.

 ### **Outline of the structure used.**

- **Categories collection**
    - This collection holds the category_name key. The categories relate to the type of resource that is being linked to, such as Books, Blogs, Events or Videos. An admin user can access this data and update and delete categories as necessary.

- **Resources collection**
    - This collection holds several keys for the resource page where the user can view all the resources in the database.
    - The data keys include the resource name, category name, topic name, date added, resource description, link to the resource and created by. 

- **Topics collection**
    - This collection holds the topic_name key. The topics relate to the type of field which the resource belongs to, such as Technology or Personal and Professional Development. An admin user can access this data and update and delete categories as necessary.

- **Users collection**
    - This collection holds several keys about the user which is provided by the user on the register page and used again on the log in page.
    - The data keys include the username, email and password. 

---

## **Existing Features**

The site has been built with responsiveness in mind and has needed the look to remain consistent across multiple devices.

### **Features Across All Pages**

#### **Navbar**

The Navbar is made up of two sections:
    
1. Brand-Logo - The navbar features the main logo for the website. This is clickable and returns the user to the main home page for the site.

2. Navigation Menu Buttons - The navbar feature the main navigation links, that allow users to move around the site. The navigation buttons show different options, depending on the status of the user:
    - Guest Users - will see the links to the Home, Login and Register pages.
    - Registered Users - will see the links to the Home, Profile, Resources and Log Out pages.
    - Admin Users - will see the links to the Home, Profile, Resources and Log Out pages, as well as a link to the Admin Dashboard page.

#### **Footer**

The footer is made up of three sections:

1. Site Title & Description - The footer contains a brief reminder of the sites title and a description of what the site is desigend to do.

2. Copyright Information - Has the built by information and copyright statement.

3. Social Media Navigation - This section holds the social icons, which link to various social media sites and the GitHub repository for the site.

#### **Return To Top Button**

- The Return To Top button, is a floating button that is controlled by JQuery code, showing a red circular button with an up arrow, in the bottom right of the webpage, once a certain scroll distance has been reached. The button when clicked, smoothly scrolls the user back to the top of the page being displayed.


### **Registration & Sign Up Page**

- The Registration page again features a simple form, where the user can input a username, email address and password. The form was designed to be as simple and fuss free as possible, in order to promote a positive user experience from the start.
- The form uses validation or error feedback when they enter information in to the input fields.
- If a user navigates to the registration page but already has an account, they can navigate to the login page via the login link. This can also be accessed via the Login page link in the navbar. 

### **Login Page**

- The login page is built around a simple form structure, where the user can enter either their username or their email address and their password.
- The form uses validation or error feedback when they enter information in to the input fields.
- If the user navigates to the login page but does not have an account, they can navigate to the registration page via the registration link. This can also be accessed via the Register link in the navbar.

### **Log Out** 
- If a user is logged in to their account, they can click on the log out button, where they will be logged out of the current session and will be taken back to the Login page.
- Should a registered user, wish to veiw the content of their profile again, they will be required to log back in to the site.

### **Home Page**

The Home page is split across three sections:

1. Brand-Logo & Description - This section gives the user an immediate sense of what the site is for and who it is aimed at. This section also hosts a call to action button promoting registration to the site.
2. Content Section - This section gives visitors a brief overview of what the may expect to be able to use the site for.
3. Weekly Featured Resources Section - This section is controlled by the site's admin and advertises examples of what the resources created on the site may contain. This section is visible by all users and is again featured, in an effort to promote registration to the site.

### **Profile Page** 
- When if the user registers an account, or logs in successfully, they are taken to their Profile page.
- The page features a header at the top, which pulls through their username form the database, giving added positivity in the user experience.
- There is a section that allows the user to update their email and password details, or delete their user account.
    - if the user chooses to edit their email address, a modal pop-up will appear and the user can input a new email address. The modal the has two buttons. One to submit the change and one to cancel the changes and take them back right back to the profile page.
    - if the user chooses to edit their password, a modal pop-up will appear and the user can input a new password. The modal the has two buttons. One to submit the change and one to cancel the changes and take them back right back to the profile page.
    - if the user chooses to delete their user account, a modal pop-up will appear and the user will be required to confirm their current password. The modal the has two buttons. One to submit the change and one to cancel the changes and take them back right back to the profile page. 
- If they have created any, the user can see all of their created resources on their profile page.
- If the user has created any resources, they will be able to see two buttons on each resource. These buttons allow editing and deleting functionality of the individual resource and are only accessible to the user that created the content and to the admin user of the site.

### **Resources Page**
- Only a logged in and registered users can view the resources page, where the created content by all users is hosted.
- If a user has created any resources, they will be able to see two buttons on each resource. These buttons allow editing and deleting functionality of the individual resource and are only accessible to the user that created the content and to the admin user of the site.
- There is a serach function user can search by category and reset the search box.
- If the user clicks on the "Add a resource" button it will take them to the Add Resource Page.
- A floating button appears on the lower right of the screen when the user starts to scroll downwards. Clicking this moves the view back up to the top of the page. This feature was added because the resources page can be quite long and the navbar is not fixed to the top of the page.

### **Add Resource Page**
- If the user clicks on the add resource button on the resources page then they will be taken to the Add Resource page.
- The add resource page is again built on a simple form structire, where the user can input the basic required information.
- The user will be required to add date to the resource in the following format:
    - Resource Title
    - Chosen Category
    - Chosen Topic
    - Date Added
    - Resource Description
    - Resource Link
- The admin user will see a checkbox which uses Materialize's switch class, to toggle the weekly featured resources on and off.
- The form uses validation or error feedback when they enter information in to the input fields.
- If the user clicks add resource button, it will add the new resource to the database.
- If the user clicks on the cancel button it will take them back to the resources page.

### **Edit Resource Page**
- The edit resources page features a simple form, where the user can edit only a resource added by them. 
- If the user has clicked on the Edit resource button, then they are taken to the edit page. They will only be able to edit the resource if they created the resource.
- The current resource information will be shown and the user can change the information and save it. This will update the database with the new information.
- The user will be able to select from the current categories and topics, as well as all additional elements that can be updated.
- The form uses validation or error feedback when they enter information in to the input fields.
- If the user clicks on the cancel button it will take them back to the resources page.

### **Admin Dashboard Page**
- This page can only be viewed by the admin user.
- From here the admin user can manage the sites categories and topics.
- The admin user can add a new category or a new topic. 
- The admin user can add a new Category if they click on the add categories button. This will take them to the Add New Category page.
- The admin user can edit current Categories. If the user clicks on the manage categories button, they will be taken to a page where they can edit or delete the details of an existing category.
- The admin user can add a new Topic if they click on the add topics button. This will take them to the Add new Topic page.
- The admin user can edit current Topics. If the user clicks on the manage topics button, they will be taken to a page where they can edit or delete the details of an existing topic.

#### **Add New Category page**
- This page can only be viewed by the admin user.
- If the admin user clicks on the add categories button on the dashboard, then this page will display.
- The Add New Category page features a simple form, where the admin user can input the basic required information. 
- The form uses validation or error feedback when they enter information in to the input fields.
- If the admin user clicks Add Category button, it will add the new category to the database in the Categories collection.
- If the user clicks on the cancel button it will take them back to the Manage resources admin dashboard page.

#### **Edit Category page**
- This page can only be viewed by the admin user.
- If the admin user clicks on the manage categories button on the dashboard, then this page will display.
- The current category information will be shown, displayed in a list of cards.
- Each category card will have two buttons. one for editing the details of the category and one for deleting the category from the database.
- The form uses validation or error feedback when they enter information in to the input fields.
- If the admin user clicks the update button, it will update the category in the database for the Categories collection.
- If the user clicks on the cancel button it will take them back to the Manage resources admin dashboard page.

#### **Add New Topic page**
- This page can only be viewed by the admin user.
- If the admin user clicks on the add topicss button on the dashboard, then this page will display.
- The Add New Topic page features a simple form, where the admin user can input the basic required information. 
- The form uses validation or error feedback when they enter information in to the input fields.
- If the admin user clicks Add Topic button, it will add the new topic to the database in the topics collection.
- If the user clicks on the cancel button it will take them back to the Manage resources admin dashboard page.

#### **Edit Topic page**
- This page can only be viewed by the admin user.
- If the admin user clicks on the manage topicss button on the dashboard, then this page will display.
- The current topic information will be shown, displayed in a list of cards.
- Each topic card will have two buttons. one for editing the details of the topic and one for deleting the topic from the database.
- The form uses validation or error feedback when they enter information in to the input fields.
- If the admin user clicks the update button, it will update the topic in the database for the Topics collection.
- If the user clicks on the cancel button it will take them back to the Manage resources admin dashboard page.

### **404 & 500 Page**
- The custom 404 & 500 Pages contain a simple word layout letting the user know of the error and a button that can be clicked to take the user back to the home page.

---

## **Future Features**

The site has been launched with a minimal viable product phase in mind. This allows the site to incorporate future features, that will improve the overall offering and user experience that is gained. Future features may include elemets such as:

- Additional profile functionality, with the option to add user profile images, a perosnal statement and options around marketing preferences.
- Functionality to retrieve and update a forgotten password.
- The ability to bookmark resources added by other users and view them in a section on the profile page.
- The ability to run additional search queries on the resources, allowing for searching by Topic, Descriptions
- Allow users to add other users as friend and add and share posts.
- Allow an administrator user the option to toggle other site users as administrators.
- Give site administrators full functionality of updating or deleting user accounts.

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