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

### Cross-User Stories**

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
![mobile-nav](/other_media/README_files/README_files/nav-mob.png) ![admin-nav](/other_media/README_files/admin-nav.png) ![desktop-nav](/other_media/README_files/desktop-nav.png)

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

Each lesson is a video so users can follow along with the course material at their own pace and revisit any topics they wish to at their leisure. Navigation buttons are placed underneath the video for convenient navigation between lessons.






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