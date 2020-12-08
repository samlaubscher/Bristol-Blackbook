<div align="center">

<img src=# alt="Main Logo">

# Bristol Blackbook

#### A Full Stack website allowing users to manage a common dataset documenting Bristol's underground Graffiti Scene.

Bristol has one of the most prolific and active graffiti scenes in the UK. The Bristol Blackbook serves to allow users to witness the styles seen on the streets of Bristol, most of which get erased within a matter of days, never to be seen again... Whether you are a part of the local culture or not, everyone should be given access to appreciate this city's underground urban artform, as well as the skill of all Bristol writers and crews putting in the work and getting up...

[**Click here to visit the Bristol Blackbook**](https://bristol-blackbook.herokuapp.com/)

##### This project was developed for my Data Centric Development project on my Full Stack Software Development course.

</div>

---

## Table of Contents

- [**1 UX**](#1-ux)

  - [**1.1 Overview**](#11-overview)
  - [**1.2 Project Goals**](#12-project-goals)
  - [**1.3 User Goals**](#13-user-goals)
  - [**1.4 Design Process**](#14-design-process)
    - [**Colour Scheme**](#colour-scheme)
    - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)
    - [**Development Stages**](#development-stages)

- [**2 Features**](#2-features)

  - [**2.1 Existing Features**](#21-existing-features)
    - Login 
  - [**2.2 Features Left to Implement**](#22-Features-left-to-impliment)
    - local

- [**3 Technologies Used**](#3-technologies-used)
  - [**3.1 Languages**](#31-languages)
    - [**HTML/HTML 5**](#html/html-5)
    - [**CSS/CSS3**](#css/css3)
    - [**JavaScript ES6**](#JavaScript-ES6)
  - [**3.2 Libraries**](#32-libraries)
    - [**Jasmine Testing Famework**](#jasmine-testing-framework)
    - [**Font Awesome**](#font-awesome)
    - [**Google Fonts API**](#Google-Fonts-API)
  - [**3.3 Tools**](#33-Tools)
    - [**VSCode**](#vscode)
    - [**Chrome DevTools**](#chrome-devtools)
    - [**Git**](#git)
    - [**GitHub**](#github)
    - [**GNU Image Manipulation Program**](#GNU-Image-Manipulation-Program)

* [**4 Testing**](#4-testing)

  - [**4.1 Completed**](#41-completed)
    - [**Manual Testing**](#manual-testing)
    - [**Automatic Testing**](#automatic-testing)
  - [**4.2 Bugs**](#42-bugs)
    - [**Fixed**](#fixed)
    - [**Still Existing**](#still-existing)

* [**5 Deployment**](#5-deployment)

  - [**5.1 Heroku**](#51-github-pages)
  - [**5.2 Local**](#52-local)

* [**6 Credits**](#6-credits)
  - [**6.1 Contents and code**](#61Contents-and-code)
  - [**6.2 Media**](#62-media)
  - [**6.3 Acknowledgements**](#63-Acknowledgements)
  - [**6.4 References**](#64-references)

---

## 1 UX

### 1.1 Overview

Bristol Blackbook was built off the idea of creating a database to document the urban artform of graffiti found on the streets of Bristol city. Often most artists upload these images to Instagram under private accounts, restricted for anonymity. This means most people cannot see them, so I wanted to create a website that maintained this idea of user privacy and was not associated with any social media platforms. This allows users to anonymously view and contribute to the content.

### 1.2 Project Goals

The purpose and goals of this project are:
- Create a full stack site that allows users to manage a common dataset about the domain of Bristol street art (graffiti).
- Implement CRUD functionality.
- Allow all users to read data from the database on the site.
- Users are able to first create an accounts, and then create, update and delete their own data.
- The sites content functionality will change for visitors and registered users.
- The site must clearly display its purpose.
- Display images effectively.
- Categorise works by artist.
- Artists assigned to crews

### 1.3 User Stories

When creating my user stories, I tried to implement the principles of Bill Wake's INVEST nmemomic for each one.
- Independant
- Negotiable
- Valuable
- Estimatable
- Small
- Testable

When necessary, I wanted to break stories down into smaller related epics.

- As a developer, I want my site to have a clearly defined purpose so users are aware of the sites functionality, maintaining a good user experience.
- As a developer, I want each of my features to have effective functionality so that users are not given an unpleasent experience.
- As a designer, I want users to register for an account so that I can personalise their experience.
- As a developer, I want users to register for an account so that I can implement user authentication, preventing unauthorised editing and deletion of data.
- As a designer, I want each work to display correct info, so that users to be able to clearly find the artist, style, year and type.
- As a designer, I want to display all content relating to each artist, crew, style or type, so that users are able to easily navigate and view this content.
- As a user, I want to see how to add content, so that I can easily contribute to the database.
- As a user, I want to 
- As a registered user, I want control over my account, so that I can easily choose to delete the account or any content I have uploaded to the website.



### 1.4 Design Process

### **Colour scheme**

### **Typography**

For the main title font used within this project, I imported a free font named 'Sprayerz' from the font folder within static/. The font I used for the main site body including the navbar was 'Kanit', supplied by Google Fonts.

The font is one of the most important aspects of the design process, so the title and text font has to fit the space theme. I used 'Audiowide' for the main title and layered multiple h2 elements offset to create a 3d drop shadow with a neon glow above. The main body text font is 'Oxanium' which is a really nice squared font that works with the digital look. 'Orbitron' is used for the score counter, the font works well with the black background as the styled line through the letters stops the font being too visually stimulating, maintaining focus on the centre of the screen.


### **Wireframes**

<details>
<summary><b>Desktop & Mobile Wireframes</b> - (click to expand)</summary>

- 

<div align="center">

<img src=# alt="Wireframe 1" width="500">
</div>

</details>

### **Development Stages**

This project was designed using an agile approach, utilisng a Kanban board to track my development progress throughout the build. You can view the board I created using Trello [here](https://trello.com/b/mH8fpkjQ/milestone-project-3).


[Back to Table Of Contents](#table-of-contents)

---

## 2 Features

### 2.1 Existing Features

### [**Home Page**]()


[Back to Table Of Contents](#table-of-contents)

---

## 3 Technologies Used

### 3.1 Languages

### [**HTML/HTML 5**](https://html.com/html5/)

HTML5 is a Hyper Text Markup Language. Roughly 16% of my code was the HTML file [index.html](index.html) as it was used to create the structured content and elements essential to build the game.

### [**CSS/CSS3**](https://www.w3.org/Style/CSS/Overview.en.html)

CSS is a Cascading Style Sheet and was implemented via the [styles.css](static\css\styles.css) file. All of the visible HTML content was positioned and styled using this language, making up roughly 24% of the entire code.

### [**JavaScript ES6**](https://www.w3schools.com/Js/js_es6.asp)

ECMAScript 6 - ECMAScript 2015, otherwise known as JavaScript 6, was used to hide the preloader upon page load.

### [**Python**](https://www.python.org/)

Python is a programming language that was used to build the functionality of this project.

### 3.2 Frameworks & Libraries

### [**Flask**](https://palletsprojects.com/p/flask/)

Flask is a Python microframework, used to create routes and template interactivity with Jinja.

### [**Jinja2**](https://palletsprojects.com/p/jinja/)

Jinja is a templating engine for Python used with Flask to render all HTML data and content within this project.

### [**Werkzeug Security**](https://palletsprojects.com/p/werkzeug/)

Werkzeug is used with Flask to secure user authentication through password hashing.

### [**MongoDB Atlas**](https://www.mongodb.com/cloud/atlas)

Atlas is the cloud hosted version of MongoDB's database service. This was used as my database for the project.

### [**PyMongo**](https://pypi.org/project/pymongo/)

PyMongo is a distribution of Python used to interact with the MongoDB database.

### [**BSON ObjectID**]()

This was used to create and parse ObjectID's from the MongoDB database.

### [**MD Bootstrap**](https://mdbootstrap.com/)

Material Design Bootstrap is a free open source CSS framework, combining styles from Material Design with the main functionality of Bootsptrap. I used MDB to fill the site with boilerplate content when building the functionality, but it was also used to create responsiveness.

### [**Font Awesome**](https://fontawesome.com/)

Font Awesome 5.8.2 was used for icons across the site.

### [**Google Fonts API**](https://fonts.google.com/)

Most of the fonts used within this project were provided by the Google Fonts API. The fonts used were 'Anton' 'Kanit', and 'Archivo Black'.

### 3.3 Tools

### [**VSCode**](https://code.visualstudio.com/)

Visual Studio Code was the Integrated Development Environment (IDE) used to write the code for this project.

### [**Chrome DevTools**](https://developers.google.com/web/tools/chrome-devtools/)

The Chrome DevTools was used for live editing and diagnosing problems. I also ran lots of auditing and testing using built in tools such as Sources, Lighthouse and Coverage.

### [**Git**](https://git-scm.com/)

The version control used in this project was Git, alongside GitHub.

### [**Github**](https://github.com/)

This repository was hosted using GitHub with Git version control.

### [**GNU Image Manipulation Program**](https://www.gimp.org/)

GNU Image Manipulation Program (GIMP) was used to create the logo and favicon website icon.

### [**Heroku**](https://www.heroku.com/)

My web application was deployed online using Heroku.

### [**Balsamiq**](https://balsamiq.com/)

Used to create the wireframes for this project

[Back to Table Of Contents](#table-of-contents)

---

## 4 Testing

### 4.1 Completed

### **Manual Testing**

### **Automatic Testing**

### 4.2 Bugs

### **Fixed**

### **Still Existing**

[Back to Table Of Contents](#table-of-contents)

## 5 Deployment

### 5.1 Heroku

This project was automatically deployed to Heroku from my GitHub repository. To do this, first I created my repository containing my ***.gitignore*** file set to ignore my virtual environment and ***env.py*** files, then followed these steps:

- Within the IDE's terminal window, create a requirements.txt file by typing ***pip3 freeze --local > requirements.txt***, and similarly create a Procfile by typing ***python app.py > Procfile***.

- Login or sign up for a new account on [Heroku](https://id.heroku.com/login), then click ***New > Create New App*** from your dashboard.

- Enter a name for your app and select the correct region before pressing ***Create App***.

- Select the ***Deploy*** tab and then click on the ***GitHub*** button under ***Deployment method***.

- Type your repository name in the search box next to the dropdown box displaying your GitHub account name. When the repository appears, click ***Connect***.

- In the ***Settings*** tab, under the ***Config Vars*** section, click the ***Reveal Config Vars*** button.

- Enter the key value pairs as found in your env.py file as such:
    - IP: 0.0.0.0
    - PORT: 5000
    - SECRET_KEY: YOURSECRETKEY
    - MONGO_DBNAME: YOUR-DATABASE-NAME
    - MONGO_URI: mongodb+srv://root:YOURPASSWORD@YOUR-CLUSTER-NAME.2qobt.mongodb.net/YOUR-DATABASE-NAME?retryWrites=true&w=majority
    - DEBUG: FALSE

- Select the ***Deploy*** tabe again and click ***Enable Automatic Deploys*** under the ***Automatic Deploys*** section. Below this is the ***Manual Deploy*** section. Select your ***Master*** branch and click ***Deploy Branch***.

- Your app will now be built, and when its completed you should see the message ***"Your app was successfully deployed"***. You can click ***View*** to launch the deployed app.

### 5.2 Locally

If you would like to run this code locally on your own machine, follow these steps:

- Follow this link to the repository for [Bristol Blackbook](https://github.com/samlaubscher/Bristol-Blackbook).

- In the top corner next to the ***About*** section, click the ***Code*** button with the downwards facing arrow icons.

- Under the ***Clone*** section, make sure the HTTPS tab is highlighted, and copy the link displayed to your clipboard. It should look like this:
    > https://github.com/samlaubscher/Bristol-Blackbook.git

- Open ***Git Bash*** in your IDE.

- First navigate to the working directory you want the files to be cloned into.

- Then type into the terminal window ***git clone {URL}*** and replace the ***{URL}*** with the link copied from the repository page.

- Upon hitting ***Enter*** the repository will be cloned into your current working directory.

- To then remove the origin link to this repository from your IDE, type ***git remote rm origin***.

- Alternatively, you can download the repository directly as a compressed ZIP folder from the ***Code*** dropdown box, underneath the ***Clone*** section. Unpack this ZIP folder into your desired location.

- When the project is successfully cloned or downloaded and opened in the correct directory, you need to install any dependancies and requirements by typing ***pip3 install -r requirements.txt*** into your IDE's terminal window.

- You next need to create an ***env.py*** file to store your environment variables. For this project, they are: 
    - import os
    - os.environ.setdefault("IP", "YOUR IP")
    - os.environ.setdefault("PORT", "5000")
    - os.environ.setdefault("SECRET_KEY", "YOURSECRETKEY")
    - os.environ.setdefault("MONGO_URI", "mongodb+srv://root:YOURPASSWORD@YOUR-CLUSTER-NAME.2qobt.mongodb.net/YOUR-DATABASE-NAME?retryWrites=true&w=majority")
    - os.environ.setdefault("MONGO_DBNAME", "YOUR-DATABASE-NAME")
    - os.environ.setdefault("DEBUG", "False")

- Then create a ***.gitignore*** file, and include this env.py file inside it to ensure your environment variables are never published publically by being pushing to GitHub.

- You are now ready run this project and push any modifications to your own repository. To run, type into the terminal ***python app.py***.

To read more about cloning repositories, you can read [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to Table Of Contents](#table-of-contents)

## 6 Credits

### 6.1 Content and code

### 6.2 Media

### 6.3 Acknowledgements

### 6.4 References

[Back to Table Of Contents](#table-of-contents)