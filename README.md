# **CodeFusion**


## **Strategy**

**CodeFusion** CodeFusion is an online learning platform designed for aspiring developers, beginners, and professionals looking to enhance their programming abilities. The CodeFusion platform offers a comprehensive suite of courses tailored to the world of coding and provides an intuitive, interactive environment, where learners can engage with high-quality course content and participate in hands-on projects within a secure and user-friendly interface.

## **Scope**

### **Learner User Stories**

#### As a user/learner I want to:

**Create and Access an Account**
- Create an account by providing my email and password
- Log in using my credentials

**Browse and Select a Course**
- Browse a list of available courses
- View detailed information about a course, including syllabus, instructor, and price
- Enroll in a course by completing the payment process

**Safely Pay for Course Access**
- Make payments securely
- Receive a confirmation message after successful payment
- Access my enrolled courses from my dashboard

---

### **Admin User Stories**

#### As an admin I want to:

**Manage user accounts:**
- view, edit, and deactivate learner accounts

**Manage Courses:**
- Create new courses by adding titles, descriptions, modules, and pricing
- Update course details and materials
- Remove courses that are outdated or no longer needed

---

### **Cross-User Stories**

#### As a learner or admin I want:

**Responsive Design**
- Access the platform on various devices (desktop, tablet, mobile),

**Intuitive Navigation**
- Navigate the platform easily using a clear and consistent menu structure,

**Secure Data Handling**
- Know that my data is handled securely,

---

## **Features**

### Navigation
![mobile-nav](/other_media/README_files/nav-mob.png) ![admin-nav](/other_media/README_files/admin-nav.png) ![desktop-nav](/other_media/README_files/desktop-nav.png)

Naviagtion is kept clean and simple. While larger screens afford the full size nav menu, nav display on smaller screens is condensed into a burger menu. It also responds to the type of user that is logged in, providing additional features for users with the appropriate permissions.

### Welcoming Landing Page
![Landing Page](/other_media/README_files/home-mob.png)

The landing page is available to all, including anonymous users. The image was chosen to give a sense of mystery with the strong Matrix vibe while the text encouraging users to start learning should make them feel like it is something that they can be a part of. Underneath there is a brief description of wha CodeFusion is, who it is for and why potential students should choose to study with CodeFusion. 

### Secure User Authentication
![Register](/other_media/README_files/register.png) ![login](/other_media/README_files/127.0.0.1_8000_accounts_login_(iPhone%206_7_8)%20(1).png) ![Password reset](/other_media/README_files/127.0.0.1_8000_accounts_password_reset_(iPhone%206_7_8)%20(1).png) ![login-validation](/other_media/README_files/login-validation.png) ![login-error](/other_media/README_files/login-error.png) ![logout-break](/other_media/README_files/logout-break.png)

Other than the landing page everything is secured behind a user account. User data is securely stored using Django-allauth.

### Dashboard
![dashboard](/other_media/README_files/dashboard1.png) ![dashboard](/other_media/README_files/dashboard2.png)

The dashboard provides a space for users to store their profile information. Some of this is taken at user signup but only basic info like username and email. The remaining fields are optional and allow users to customise their profile as much or as little as they like.

The second section of the dashboard provides a quick glance at the courses that the user is currently enrolled on.

### Courses
![courses](/other_media/README_files/courses.png) ![course-mob](/other_media/README_files/course-mob.png) ![course-access](/other_media/README_files/course-access-denied.png)

The course list clearly displays courses, giving users a clear indication of what the course is about at a glance. A brief description is included to give the user a bit more information on what is covered and who the course is aimed at. Finally, the price and add to basket button at the bottom. 

As these cards are also links to the course content, should a user attempt to access a course that they ae not enrolled in a simple message is displayed to indicate that the content is restricted. This message automatically times out after a few seconds.

### Lessons
![portrait](/other_media/README_files/lesson-portrait.png) ![landscape](/other_media/README_files/lesson-landscape.png)

Each lesson is a video so users can follow along with the course material at their own pace and revisit any topics they wish to at their leisure. Navigation buttons are placed underneath the video for convenient navigation between lessons. Whilst viewing is possible in prtrait mode, landscape is very much recommended.

### Basket
![basket](/other_media/README_files/basket.png)

Courses that have been aded to the basket appear here. Each course gives some information about the course such as title, instructor and price. There is also a remove button should users change their mind. Each item added to the basket will bring the user to the basket so a continue browsing button is placed at the bottom for conveniently returning to brose more courses. When the user is ready to checkout the checkout button will take them to process payment.

### Checkout
![Checkout](/other_media/README_files/checkout.png) ![Checkout](/other_media/README_files/checkout-success.png) ![Checkout](/other_media/README_files/checkout-cancel.png)

Stripe checkout takes care of payments. Form is fully validated and secure and provides options for remembering users and faster checkouts using link. 

If a user cancels they are taken back to the site via a cancel confirmation page which automatically redirects to the basket after a few seconds. If this fails there is a button that can be clicked or the navigation menu can be used so the user isnt stranded. 

Once checkout is completed a success message is displayed for a few seconds before automatically redirecting back to the dashboard where the user can see theie purchased courses in the enrollment list. Again, should the redirection fail there is a button or the navigation menu to rescue the user.

### Course Management
![Admin](/other_media/README_files/admin-panel.png) ![Course Management](/other_media/README_files/course-admin.png) ![Course Modal](/other_media/README_files/course-admin-modal.png) ![Lesson Management](/other_media/README_files/lesson-admin.png)

Currently, admins can access the course management section from here. From here admins have full control over CRUD functionality for all course and lesson content. The delete button on courses is defensively programmed to avoid accidental deletions.

## Structure
The schema for this project called for a variety of relationship types between tables. 

![schema](/other_media/README_files/lucidchart_schemas.png)

The flow chart

![flowchart](/other_media/README_files/CodeFusion_FlowChart.png)

## Skeleton

![figmahome](/other_media/README_files/CodeFusionIndex.png)

![figmaregister](/other_media/README_files/CodeFusionRegister.png)

![figmalogin](/other_media/README_files/CodeFusionLogin.png)

![figmadashboard](/other_media/README_files/CodeFusionDashboard.png)

![figmacourses](/other_media/README_files/CodeFusionCourses.png)

![figmalessons](/other_media/README_files/CodeFusionLessons.png)

![figmabasket](/other_media/README_files/CodeFusionBasket.png)

![figmacheckout](/other_media/README_files/CodeFusionCheckout.png)

## Surface

![Landing Page](/other_media/README_files/home-mob.png) ![login](/other_media/README_files/127.0.0.1_8000_accounts_login_(iPhone%206_7_8)%20(1).png) 

![dashboard](/other_media/README_files/dashboard1.png) ![dashboard](/other_media/README_files/dashboard2.png)

![course-mob](/other_media/README_files/course-mob.png) ![course-tab](/other_media/README_files/course-tab.png) 

![portrait](/other_media/README_files/lesson-portrait.png) ![landscape](/other_media/README_files/lesson-landscape.png)

## Testing

### User Stories

#### Learner User Stories

| Expectation                                                                                                                                                    | Implementation |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| I want to create an account by providing my email and password, so that I can securely access and personalize my learning experience.                          |Users are able to create an account via the register page. Anonymous users cannot access restricted pages, even with a url|
| I want to log in using my credentials, so that I can access my enrolled courses and progress.                                                                  |Once registered users can login to their account securely                |
| I want to reset my password through my registered email, so that I can regain access to my account without hassle.                                             |Reghistered users can request a password reset email from their user dashboard                |
| I want to browse a list of available courses, so that I can choose courses that interest me.                                                                   |The courses page provides a list of all courses that are available to study                |
| I want to view detailed information about a course, including syllabus, instructor, and price, so that I can make an informed decision before enrolling.       |Each course has a title, image and description that give the user a clear idea of the course content and the level of difficulty|
| I want to enroll in a course by completing the payment process, so that I can gain access to course materials and start learning.                              |Users can pay for courses in order to gain access to the content|
| I want to make payments securely so that I can ensure my financial information is protected during transactions.                                               |Payments are made secure using Stripe checkout. Users can be confident their data is safe                |
| I want to receive a confirmation message after successful payment, so that I know my enrollment has been processed.                                            |Users are taken to a confirmation message after successful payment                |
| I want to navigate through different modules or sections within a course, so that I can follow the course content easily.                                      |Course lessons are ordered and navigation on each lesson page helps users stay on track                 |
| I want to update my profile information, such as my name and contact details, so that my account information remains current and accurate.                     |Users are able to update their profile from the dashboard                |
| I want to view a history of all courses I have enrolled in, so that I can easily revisit past courses or track my learning progress.                           |Enrolled course are displayed in the user dashboard                |

#### Admin User Stories
| Expectation                                                                                  | Implementation |
|----------------------------------------------------------------------------------------------|----------------|
| I want to create new courses by adding titles, descriptions, modules, and pricing, so that I can expand the platform’s offerings to attract more learners. |Admin users are able to access the Course Management interface and create courses and lesson content                |
| I want to update course details and materials, so that I can ensure that the content remains current and relevant. |Admin users are able to access the Course Management interface and edit courses and specific lesson content                |
| I want to remove courses that are outdated or no longer needed, so that the platform remains organized and focused on quality content. |Admin users are able to access the Course Management interface and delete courses               |
| I want to add, edit, or reorder modules within a course, so that the course structure is logical and effective for learners. |Admin users are able to access the Course Management interface and edit specific lesson content                |

#### Cross-user Stories
| Expectation                                            | Implementation |
|--------------------------------------------------------|----------------|
| I want to access the platform on various devices (desktop, tablet, mobile), so that I can use the platform conveniently from anywhere. |The platform has been designed and tested throughout to ensure compatibility across a range of devices and screen sizes                |
| I want to navigate the platform easily using a clear and consistent menu structure, so that I can find the features and information I need without confusion. |Navigation is simple and consistent, changing only depending on screen size or for additional admin navigation                |
| I want to know that my data is handled securely, so that I can trust the platform with my personal and financial information. |Django allauth and Stripe are well regarded as being safe and secure means of handling user data                |


### Functionality
![test sheet one](/other_media/README_files/test-sheet-1.png)

![test sheet one](/other_media/README_files/test-sheet-2.png)

![test sheet one](/other_media/README_files/test-sheet-3.png)

### Lighthouse Results
![Lighthouse](/other_media/lighthouse/desktop/home.png) ![Lighthouse](/other_media/lighthouse/desktop/register.png) ![Lighthouse](/other_media/lighthouse/desktop/login.png)
![Lighthouse](/other_media/lighthouse/desktop/dashboard.png) ![Lighthouse](/other_media/lighthouse/desktop/courses.png) ![Lighthouse](/other_media/lighthouse/desktop/lesson.png)
![Lighthouse](/other_media/lighthouse/desktop/basket.png) ![Lighthouse](/other_media/lighthouse/desktop/course-admin.png) ![Lighthouse](/other_media/lighthouse/desktop/lesson-admin.png)

### Validator Results
![HTML Validator](/other_media/validation/index.png) ![HTML Validator](/other_media/validation/dashboard.png)
![HTML Validator](/other_media/validation/courses.png) ![HTML Validator](/other_media/validation/lessons.png)
![HTML Validator](/other_media/validation/basket.png) ![HTML Validator](/other_media/validation/admin-create.png)
![HTML Validator](/other_media/validation/course-admin.png) ![HTML Validator](/other_media/validation/css.png)

The HTML validator was unable to assess and validate by URL for any pages that required authentication to access. In order to assess the HTML I copied the code from the dev tools in Chrome and pasted into the validator. 

## Deployment and Local Development

## Deployment & Local Development

### Github

This project can be cloned or forked in order to make a local copy on your own system.

You will need to install packages found within the *requirements.txt* file and set environment variables in an *env.py* file saved to the root directory.

#### **How to Fork**

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.

You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [CodeFusion GitHub Repository](https://github.com/GitHubWestie/milestone-project-four)
2. At the top of the Repository (not the top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

#### **How to Clone and Setup for Local Development**

There are several methods available to clone a repository but this guide will use [Visual Studio Code](https://code.visualstudio.com/).

1. Go to the [CodeFusion GitHub repository](https://github.com/GitHubWestie/milestone-project-four) 
2. Copy the url from the address bar or click on the green 'code' button and copy the url from there
3. In VS Code select Clone Git Repository from the welcome screen or push ctrl + shift + P on your keyboard to open the pallette and type 'clone'. From the list select Git:clone and paste in the repository URL. Push enter or click the URL
4. VS Code will prompt you to select a destination folder for the cloned repository. Once selected the repo will be cloned and VS Code will prompt again to open the cloned repository.
5. It is advisable to setup a virtual environment before installing packages. Hit ctrl + shift + P and in the pallette type Python:Create environment. Hit enter or click and choose venv, then select your Python interpreter. As there is a requirements.txt file in the repository you may be prompted to select dependencies to install. If so check the box for requirements.txt and give VS Code a moment to set everything up. When the environment is ready VS Code will display a small message in the corner and a (.venv) should appear in your terminal.
6. If the option to install dependencies wasnt offered then once the venv is setup go to your terminal and type:
    * `pip install -r requirements.txt`

   Wait while dependencies are installed
7. Create env.py file in root directory and assign environment variables
    * `import os`
    * `os.environ['SECRET_KEY'] = 'yourdjangosecretkeygoeshere'`
    * `os.environ['STRIPE_SECRET_KEY'] = 'yourstripesecretkeygoeshere'`
    * `os.environ['STRIPE_PUBLISHABLE_KEY'] = 'yourstripepublishablekeygoeshere'`
8. Before running the server initialise a database. In the terminal type:
    * `python manage.py makemigrations`

    Once that has completed, in the terminal type:
    * `python manage.py migrate`

    You should now have an empty sqlite3 database for local development
9. Make sure DEBUG is set to True in settings.py and in the terminal run:
    * `python manage.oy runserver`

    VS Code should prompt to open a browser but if not ctrl + click the development server address in the terminal. If you encounter a warning from Django regarding allowed hosts go back to settings.py and in the ALLOWED_HOSTS list add your local IP address.
10. The final thing to do is create an admin user. In the terminal type:
    * `python manage.py createsuperuser`

    You will be prompted for some credentials (email isnt necessary, push enter to skip and you will not be able to see the password you type in, this is normal)
11. Run the server if it isnt already running and login with the superuser credentials. If you need to access the django admin features just add /admin to the local address in the browser address bar.
12. In your IDE terminal type the following commands to setup your repository:
    * `git remote add origin https://github.com/your-username/new-repo.git`
    * `git push -u origin main`


## Technologies

### Languages Used
- HTML
- CSS
- JavaScript
- Python

### Frameworks
- [Django 5.1](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Stripe](https://docs.stripe.com/checkout/quickstart)
- [Postgres](https://www.postgresql.org/)

### Libraries
- [FontAwesome](https://fontawesome.com/)

### Programs and Services
- [Figma](https://www.figma.com/)
- [GIMP](https://www.gimp.org/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
- [GitHub](https://github.com/)
- [Google Dev Tools](https://developer.chrome.com/docs/devtools)
- [Heroku](https://www.heroku.com/)
- [pip](https://pypi.org/project/pip/)

### Testing and Validation
- [W3C Markup Validation Service](https://validator.w3.org/)
- 

## Credits

[Django Documentation](https://www.djangoproject.com/)

[Django allAuth Documentation](https://docs.allauth.org/en/latest/)

[Bootstrap Documentation](https://getbootstrap.com/)

[Dave Gray Course Content](https://youtube.com/@davegrayteachescode?si=b7s8JX9LIh0yrzWU)

[Django course image courtesy of Roberto Huertas](https://icon-icons.com/users/QYVbFw10tinSxMN47fONm/icon-sets/)

[HTML course image courtesy of Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTML5_Badge.svg)

[Image resizing courtesy of TinyPNG](https://tinypng.com/)

[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 

[StackOverflow](https://stackoverflow.com/questions/39009638/how-to-edit-django-allauth-default-templates)

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

[Stripe](https://docs.stripe.com/checkout/quickstart)

[Matt Freire - Django Stripe setup](https://youtu.be/722A27IoQnk?si=hdCXsV2F4b041ZzA)

[AdamJ.eu](https://adamj.eu/tech/2022/10/06/how-to-safely-pass-data-to-javascript-in-a-django-template/#:~:text=Django's%20template%20system%20only%20escapes,recommend%20you%20never%20do%20it.)

[Markus Spiske](https://www.pexels.com/photo/black-and-white-striped-textile-193350/)

[Image Resizer](https://imageresizer.com/)

[Scaler Topics - Riya Verma - JavaScript Reference](https://www.scaler.com/topics/javascript-hide-element/)

[AmIresponsive](https://ui.dev/amiresponsive)