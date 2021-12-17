# Application Testing Details

[Main README.md file](/README.md)

[View live version of website via Heroku](https://tech-growth-mindset.herokuapp.com/)

---

## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Manual testing](#manual-testing)
* [Bugs and Fixes](#bugs-and-fixes)
* [Further testing](#further-testing)

---

#### *New Visitor*
1. As a first time visitor, I want the main purpose of the site to be immediately clear.
2. As a first time visitor, I want the look of the site to be visually appealing.
3. As a first time visitor, I want the layout of the site to be well structured and easy to navigate.
4. As a first time visitor, I want to have an idea of the content that the site offers, before deciding to register.
5. As a frist time visitor, I want to be able to easily find and use the registration page, if I choose to register.
6. As a first time visitor, I want to see ways of communicating with the site's creators, via social media or a contact page.

- The Home Page has been designed to be simplistic, yet fully evidence what the site is about. In addition to this, the purpose of the site is also mentioned in the Footer. The colour palette used, was chosen to keep the site as visually appealing as possible. The home page is essentially split in to two sections, the first being the main title and image for the site with a call to action button, the second being a section that hosts the weekly featured content, controlled by the sites admin. This gives a visitor an idea of what content the site holds. The Footer hosts a contact us section where users can reach out to the sites creator. Non-registered users will also have access to the registration page through a link in the navbar.

    - [Navbar](/documentation/images/testing-images/navbar.png)
    - [Home Page](/documentation/images/testing-images/home-page.png)
    - [Weekly Featured Section](/documentation/images/testing-images/weekly-featured.png)
    - [Footer](/documentation/images/testing-images/footer.png)
    - [Registration Page](/documentation/images/testing-images/registration-page.png)

#### *Registered User*
1. As a registered user, I want to be able to login with a set of registered credentials.
2. As a registered user, I want to be able to logout of my account.
3. As a registered user, I want to be able to change my user credentials.
4. As a registered user, I want to be able to see all resources posted by other members.
5. As a registered user, I want to be able to create a new resource to be added to the library.
6. As a registered user, I want to be able to edit or delete posts that I have created myself.
7. As a registered user, I want to be able to see a profile page where I can review my own resource posts.
8. As a registered user, I want to be able to quickly serach for relevant resources.
9. As a registered user, I want to be able to delete my account in full, if I no longer wish to remain a member.

- Once Registered, users will be taken to their profile page. From here, they will have the functionality to log back out via the Navbar or manage their user account details. Users when managing their account will have three options: 1. Update their email address. 2. Update their password. 3. Delete their user account.
- Registered users will alsb be able to see a list of their own submitted resources on their profile page, as well as have the functionality to update or delete each individual resource that they have created.
- Registered users will have access to a specific resources page, where all user submitted resources are listed. If the user has nno resources already created, they will be able to do so, via the Add New Resource button. The Add New Resource will take the user to a form based page, where they can input the necessary details of the resource they would like to create. This page features a serch feature that allows user to search for specific resources by category. The page also features the update and delete functionality on resources created by the specific user

    - [Navbar](/documentation/images/testing-images/navbar.png)
    - [Profile](/documentation/images/testing-images/profile-page.png)
    - [Profile Management Section](/documentation/images/testing-images/profile-management.png)
    - [Update Email](/documentation/images/testing-images/update-email.png)
    - [Change Password](/documentation/images/testing-images/change-password.png)
    - [Delete Account](/documentation/images/testing-images/delete-account.png)
    - [User Created Resources](/documentation/images/testing-images/my-resources.png)
    - [Edit Resource](/documentation/images/testing-images/edit-resource-page.png)
    - [Resources Page](/documentation/images/testing-images/resources-page.png)
    - [Add New Resource Button](/documentation/images/testing-images/add-new-resource.png)
    - [Add Resource Page](/documentation/images/testing-images/add-resource.png)
    - [Search Function](/documentation/images/testing-images/search-box.png) 

#### *Site Administrator*
1. As a site Administrator, I would want to be able to control the main functionality of the site, including adding new categories and topics.
2. As a site Administrator, I would want to be able to edit or delete categories and topics.
3. As a site Administrator, I would want to be able to control the resources added and select weekly featured resources.
4. As a site Administrator, I would want to be able to view all resource posts added by users and delete where necessary, keeping the site up-to date.
5. As a site Administrator, I would want to be able to add new users or delete users who have issues with functionality.

- Users registered as the administrator for the site will have access to all content that a reqular user would, with the addition of access to an admin dashboard.
- From the admin dashboard, the administrator can access the management section of the site, where both the categories and topics can be managed. Management of both has been designed in exactly the same way, so that functionality remains consistent.
- When looking to add a new category or topic, the admin user can click on a modal button, that gives suggestions of what to add for that specific feature. When clicking on the add category button, they are met with the add category page. The add topic button takes the user to a page of theeaxct same styling, where they can add a new topic.
- When the admin user clicks on the manage categories or topics buttons, they are met with the manage categories or topics pages. Thes pages are both exactly the same in styling.
- The admin user has also been given access to additional functionality, when on the edit resource page. The admin user can toggle on or off, the switch that selects the specific resource as part of the weekly featured resources.

    - [Admin Dashboard](/documentation/images/testing-images/admin-dashboard.png)
    - [Admin Management](/documentation/images/testing-images/admin-management.png)
    - [Category Modal](/documentation/images/testing-images/category-modal.png)
    - [Topic Modal](/documentation/images/testing-images/topic-modal.png)
    - [Add Category](/documentation/images/testing-images/add-category.png)
    - [Category Management](/documentation/images/testing-images/category-management.png)
    - [Edit Category](/documentation/images/testing-images/edit-category.png)
    - [Weekly Featured Switch](/documentation/images/testing-images/weekly-featured-toggle.png)

---

## Testing and Validation

### Lighthouse (Google Dev Tools)

- The Lighthouse Report for the site's main home page on Mobile was as follows:
   - [Mobile Lighthouse Report](/documentation/images/testing-images/lighthouse-mobile-home.jpg)

- The Lighthouse Report for the site's main home page on Desktop was as follows:
   - [Mobile Lighthouse Report](/documentation/images/testing-images/lighthouse-desktop-home.jpg)

### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
- [Am I Responsive ](/documentation/images/testing-images/am-I-responsive-home.png)

### JavaScript
- [JSHint](https://jshint.com/)
   - [JavaScript Validation](/documentation/images/testing-images/jshint.png)
   - Addressing errors and warnings: 
      - In the initial testing a warning for ''let' is available in ES6 (use 'esversion: 6') is presented. If the following shrot line of code is added, /*jshint esversion: 6 */ to the top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features, the the initial warning no longer appears and can be safely ignored.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored. 

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- To validate the CCS code of the project pasting code in by direct input method.
- The validation of the css file shows no issues and passes its checks in full
- [CSS Validation](/documentation/images/testing-images/css-validation.png)

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- Testing and results per page:
   - Home Page - No errors in testing.
      - [Home Page Validation](/documentation/images/testing-images/home-page-validation.png)
   - Log In Page - No Errors in testing.
      - [Log In Page Validation](/documentation/images/testing-images/login-page-validation.png)
   - Register Page - No errors in testing.
      - [Register Page Validation](/documentation/images/testing-images/register-page-validation.png)
   - Profile Page - No errors in testing.
      - [Profile Page Validation](/documentation/images/testing-images/profile-page-validation.png)
   - Admin Dashboard Page - No errors in testing.
      - [Admin Dashboard Page Validation](/documentation/images/testing-images/admin-page-validation.png)
   - Resource Page - No errors in testing.
      - [Resource Page Validation](/documentation/images/testing-images/resource-page-validation.png)
   - Add Resources Page - No errors in testing.
      - [Add Resources Page Validation](/documentation/images/testing-images/add-resource-validation.png)
   - Edit Resource Page - No errors in testing.
      - [Edit Resource Page Validation](/documentation/images/testing-images/edit-resource-validation.png)
   - Add Category Page - No errors in testing.
      - [Add Category Page Validation](/documentation/images/testing-images/add-category-validation.png)
   - Add Topic Page - No errors in testing and finally
      - [Add Topic Page Validation](/documentation/images/testing-images/add-topic-validation.png)
   - Manage Categories Page - No errors in testing and finally
      - [Manage Categoryies Page Validation](/documentation/images/testing-images/manage-categories-validation.png)
   - Manage Topics Page - No Errors in testing and finally
      - [Manage Topics Page Validation](/documentation/images/testing-images/manage-topics-validation.png)
   - Error Pages - No errors in testing and finally
      - [Error Pages Final](/documentation/images/validator_screenshots/html_validator_404_page_test.png)

### Python
- [PEP8 Online](http://pep8online.com/) - Pythoon file is PEP8 compliant
   - [Python Validation](/documentation/images/testing-images/pep8-validation.png)

---
## **Manual testing**
Manual testing of all elements and functionality on every page
1. Logo - click on the logo, returns to the “Home” section on all pages.
2. Navbar 
   - if *a new visitor* clicks on the Home link on any page - They are redirected to the Home page.
   - if *a new visitor* clicks on the Login link on any page - They are redirected to the Login page.
   - if *a new visitor* clicks on the Register link on any page - They are redirected to the Registration page. 
   - if *Registered user* clicks on the Resource link - They are redirected to the Resources page.
   - if *Registered user* clicks on the Profile link - They are redirected to the Profile page.
   - if *Registered user* clicks on the Log Out link - They are logged out of their account and redirected to the Login page.
   - if *Admin user* clicks on Admin link - They are redirected to the Admin Dashboard page.
3. Footer 
   - if *any user* clicks on the Instagram link - They will be redirected to the generic site for Instagram.
   - if *any user* clicks on the LinkedIn link - They will be redirected to the LinkedIn Page for Andrew Llewellyn.
   - if *any user* clicks on the Twitter link - They will be redirected to the generic site for Twitter.
   - if *any user* clicks on the GitHub link - They will be redirected to the GitHub Profile Page for Andrew Llewellyn.
4. Floating to top button 
   - When the Return To Top button appears on the screen - clicking the button, moves the view back up to the top of the page.
5. Home Page
   - if *any user* clicks on the Registration Button - They are redirected to the Registration page.
   - if *any user* clicks on each Weekly Featured Resource card link - They are redirected to the specified external link.
6. Registration & Sign Up Page
   - if *a new visitor* types in a "Username", "Email" and "Password" to the required fields - validation is given if correct and feedback is given if incorrect.
      - if the visitor then clicks on the "Register" button, their details are added to the database They are redirected to the Profile page and feedback is given to the user that they are registered.
   - if *any user* clicks on the "Login Here" link - They are redirected to the Login page.
7. Log in Page
   - if *Registered users* type in their user details in the "Username" and "Password" fields validation is given if correct and feedback is given if incorrect.
      - if the user then clicks on the "Login" button, the user is logged in. They are redirected to the Profile page and feedback is given to the user that they are logged in.
   - if *any user* clicks on the "Sign up here!" link - They are redirected to the Registration page.
8. Profile Page 
   - if *Registered user* clicks on the "Update Email" button - They are faced with a pop-up to enter a new Email address.
   - if *Registered user* clicks on the "Update Password" button - They are faced with a pop-up to enter a new Password.
   - if *Registered user* clicks on the "Delete Account" button - They are faced with a pop-up to delete the account.
      - if the user types in the correct user password and clicks the "Delete" button - the account is deleted from the database and a is given to the user, who is redirected to the Registration page.
      - if the user clicks on "Cancel" - they go back to the Profile page
9. Resources Page
   - if *Registered user* types text in the search field and click on the "Search" button", the relevant matching resource is shown. If there are no matching resources, the user is alerted to try again or add a new resource. 
   - if the user clicks on the "Reset" button, the search field is reset.
   - if *Registered user* clicks on the "Add New Resource" - They are redirected to the Add Resource page.
   - if *Registered user* clicks on the Resource Link button on the Resource card - They are redirected to the specified external link.
   - if *Registered user* created the resource - they can see the Edit & Delete buttons. This functionality is also visible to any admin of the site.
      - if the user clicks on each Resource card "Delete" Button - The user is show a modal where they must confirm deletion. If deletion is confirmed the resource is deleted, removed from the database and the user gets a confirmation. If deletion is cancelled, the user is taken back to the resources page.
      - if the user clicks on each Resource card "Edit" Button - They are redirected to the Edit Resource page.
10. Add Resource Page
   - if *Registered user or Admin User* clicks on "Choose Category" and "Choose Topic" they can select a current category or topic.
   - if *Registered user or Admin User* types text in to the input fields, validation is given if correct and feedback is given if incorrect.
   - if *Registered user or Admin User* wants to select a date, a date picker opens with the current date and a date can be selected.
   - if *Registered user or Admin User* clicks on the "Add Resource" button, a new resource is added to the database and a success message is given to the user.
   - if *Registered user or Admin User* clicks on cancel - go to Resources Page.
   - if *Admin User* clicks on the Weekly Featured resource toggle button, the resource is added to weekly featured section of home page.
11. Edit Resource Page
   - a view of the current details of the resource appears.
   - if clicking on "Choose Category" and "Choose Topic" they can select a current category or topic.
   - if typeing in text in fields, validation is given if correct and feedback is given if incorrect.
   - if the user wants to select a date, a date picker opens with the current date and a date can be selected.
   - if clicking on the "Update Resource" button, the resource is updated in the database and a success message is given to the user.
   - if clicking on cancel - the user is taken back to the Resources Page.
   - if *Admin User* clicks on the Weekly Featured resource toggle button, the resource is added to weekly featured section of home page.
12. Manage Resource Admin Dashboard Page
   - if *Admin user* clicks the info button in the category management section, a modal pop-up appears, providing info about Categories.
   - if *Admin user* clicks the "Add Category" button, they are redirected to the Add Category page. 
   - if *Admin user* clicks the "Manage Categories" button in the Category section, go Current Categories page.
   - if *Admin user* clicks the "Edit" button in the Category section, they are redirected to the edit categoory page.
   - if *Admin user* clicks the "Delete" button in the Category section, the category is deleted.
   - if *Admin user* clicks the info button, in the topic management section, a modal pop-up appears, providing info about Topics.
   - if *Admin user* clicks the "Add Topic" button, they are redirected to the Add Category page. 
   - if *Admin user* clicks the "Manage Topics" button in the Category section, go Current Topics page.
   - if *Admin user* clicks the "Edit" button in the Topic section, they are redirected to the edit topic page.
   - if *Admin user* clicks the "Delete" button in the Topic section, the topic is deleted.
14. Add New Category page
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* click on the "Add Category" button, a new category is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel, they are redirected back to Admin Dashboard Page.
15. Edit Category page
   - view current details of category
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect. 
   - if *Admin user* click on the "Update Category" button, the category is updated in the database and a success message is given to the user.
   - if *Admin user* click on cancel they are redirected back to Admin Dashboard Page.
16. Add New Topic page
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* click on the "Add Topic" button, a new Topic is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel, they are redirected back to Admin Dashboard Page
17. Edit Topic page
   - view current details of category
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect. 
   - if *Admin user* click on the "Update Topic" button, the Topic is updated in the database and a success message is given to the user.
   - if *Admin user* click on cancel they are redirected back to Admin Dashboard Page.

---

## **Bugs and Fixes**

### Known Bugs
- A bug was picked up, when testing the Form Validation for the select dropdowns on the create and edit resource pages. If a cateogry or topic is selected, border-bottom does not change to a validated state of green, it instead changes to an invalidated state of red. This was discusssed in depth with the support team at the Code Institue who tested the functionality their end. Upon testing their end, the validation was working as it should. This prompted further testing on my side with different devices, and the validation again appeared to work as it should. The issue appeared to be based on something from my system, and as of yet, I am unable to find a reason for it. The issue also happens when testing on other browsers on my system. As it stands, the user will see the validation work correctly.

---

### Deployment
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable in app.py file is set to False.
- Confirmed that there is no difference between the deployed version and the development version.