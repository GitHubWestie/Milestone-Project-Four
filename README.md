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
![Checkout]()


### Admin Panel
![Admin]()


### Course Management
![Course Management]()


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

![course-mob](/other_media/README_files/course-mob.png)

![portrait](/other_media/README_files/lesson-portrait.png) ![landscape](/other_media/README_files/lesson-landscape.png)

## Testing

### User Stories

#### Anonymous User Stories


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



** Credits

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