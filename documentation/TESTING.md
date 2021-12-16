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


## Testing and Validation

### Lighthouse (Google Dev Tools)



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
      - [Edit Resource Page Validation](#)
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