<div align="center">

<img src="./static/images/readme/bristol-blackbook.jpg" alt="Main Logo" width="700">

# Bristol Blackbook

#### A Full Stack website allowing users to manage a common dataset documenting Bristol's underground Graffiti Scene.

Bristol has one of the most prolific and active graffiti scenes in the UK. The Bristol Blackbook serves to allow users to witness the styles seen on the streets of Bristol, most of which get erased within a matter of days, never to be seen again... Whether you are a part of the local culture or not, everyone should be given access to appreciate this city's underground urban artform, as well as the skill of all Bristol writers and crews putting in the work and getting up...

[**Click here to visit the Bristol Blackbook**](https://bristol-blackbook.herokuapp.com/)

##### This project was developed for my Data Centric Development project on my Full Stack Software Development course.

<img src="./static/images/readme/amiresponsive.jpg" alt="Main Logo" width="700">

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
    - [**Intro Index Landing Page**](#intro-index-landing-page)
    - [**All Works Main Home Page**](#all-works-main-home-page)
    - [**Register & Login Pages**](#register-&-login-pages)
    - [**Profile Page**](#profile-page)
    - [**Logout**](#logout)
    - [**New Upload Page**](#new-upload-page)
    - [**Work Page**](#work-page)
    - [**Edit Work Page**](#edit-work-page)
    - [**Add Artist Page**](#add-artist-page)
    - [**Artists Page**](#artists-page)
    - [**Artist Page**](#artist-page)
    - [**Edit Artist Page**](#edit-artist-page)
    - [**Add Crew Page**](#add-crew-page)
    - [**Crews Page**](#crews-page)
    - [**Crew Page**](#crew-page)
    - [**Edit Crew Page**](#edit-crew-page)
    - [**Add Style Page [Admin Only]**](#add-style-page-[admin-only])
    - [**Styles Page**](#styles-page)
    - [**Style Page**](#style-page)
    - [**Edit Style Page [Admin Only]**](#edit-style-page-[admin-only])
    - [**Add Type Page [Admin Only]**](#add-typee-page-[admin-only])
    - [**Types Page**](#types-page)
    - [**Type Page**](#type-page)
    - [**Edit Type Page [Admin Only]**](#edit-type-page-[admin-only])
    - [**Admin Panel page [Admin Only]**](#admin-panel-page-[admin-only])
    - [**Header Image**](#header-image)
    - [**Navbar**](#navbar)
    - [**Footer**](#footer)
    - [**404 Error Handling Page**](#404-error-handling-page)
  - [**2.2 Features Left to Implement**](#22-Features-left-to-impliment)
    - [**Bristol Paint Shops Page**](#bristol-paint-shops-page)
    - [**Work Rating System**](#work-rating-system)
    - [**Comments Section On Works**](#comments-section-on-works)

- [**3 Technologies Used**](#3-technologies-used)
  - [**3.1 Languages**](#31-languages)
    - [**HTML/HTML 5**](#html/html-5)
    - [**CSS/CSS3**](#css/css3)
    - [**JavaScript ES6**](#JavaScript-ES6)
    - [**Python**](#Python)
  - [**3.2 Frameworks & Libraries**](#32-frameworks-&-libraries)
    - [**Flask**](#Flask)
    - [**Jinja2**](#jinja2)
    - [**Werkzeug Security**](#Werkzeug-Security)
    - [**MongoDB Atlas**](#mongodb-atlas)
    - [**PyMongo**](#pymongo)
    - [**BSON ObjectID**](#bson-objectid)
    - [**MD Bootstrap**](#md-bootstrap)
    - [**Font Awesome**](#font-awesome)
    - [**Google Fonts API**](#Google-Fonts-API)
  - [**3.3 Tools**](#33-Tools)
    - [**VSCode**](#vscode)
    - [**Chrome DevTools**](#chrome-devtools)
    - [**Git**](#git)
    - [**GitHub**](#github)
    - [**GNU Image Manipulation Program**](#GNU-Image-Manipulation-Program)
    - [**Heroku**](#heroku)
    - [**Balsamiq**](#balsamiq)

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

Bristol Blackbook was built from the idea of creating a database for documenting the urban artform graffiti, found on the streets of Bristol city. 

Often most artists upload these images to Instagram under private accounts, restricted for anonymity. This means most people cannot see them, so I wanted to create a website that maintained this idea of user privacy and was not associated with any social media platforms. This allows users to anonymously view and contribute to the content. 

I chose the name Bristol Blackbook as the blackbook is famously where graffiti writers practice their work, and often they collect the tags and works of other graffiti writers in these books when they meet others. For a graffiti writer, blackbooks are a good way of personally archiving a section of their history in graffiti, they capture the artists works permanently, their progression, and they often hold the memory of all artists that have contributed to the book.

### 1.2 Project Goals

The purpose and goals of this project are to:
- Create a full stack site that allows users to manage a common dataset about the domain of Bristol street art (graffiti).
- Implement CRUD functionality.
- Allow all users to read data from the database on the site.
- Allow users to first create an account, and then create, update and delete their own data.
- Modify the sites content and functionality based on visitors and registered users.
- Clearly display the sites purpose.
- Display images effectively.
- Categorise and group works by artist, style & type.


### 1.3 User Stories

### First Time Users

- As a user, I want a site to have a clearly defined purpose when I first enter so that I know what I am viewing.
- As a user, I want all functionality on the site to work to avoid a bad experience.
- As a user, I want to be able to browse all works in the db.
- As a user, I want to clearly see the artist name, style, type and year painted for each work.
- As a user, I want to be able to easily browse all individual artists, crews, styles amd types in the db.
- As a user, I want to register for an account so that I can contribute to the database.
- As a user, I want to see how to add content, so that I can easily contribute to the database.

### Returning Users

- As a returning user, I want to log into my account and be presented with my own profile page.
- As a returning user, I want to see what I have uploaded to the database on this profile page.
- As a returning user, I want control over my data, so that I can easily choose to delete the account or any content I have uploaded to the website.


### 1.4 Design Process

### **Logo**

I designed a logo for the site using the font 'Sprayerz' ontop of a spray type pattern, created in GIMP.

<div align="center">
<img src="./static/images/readme/logo-black.jpg" alt="Main Logo" width="200">
</div>

### **Colour scheme**

Fitting with the name Blackbook, I decided to design the site with a black background. I also implemented a pink/purple color scheme, taking inpiration from one of the Materialize gradient buttons used on the main welcome page and works page for the Enter & Sort By buttons.

- #000000 - Black was used for the main body background.
- #9A9A9A - Grey was used for some of the text and social icons.
- #ffffff - White was used for the main body text color.
- #D86FD2 - Pink was the first shade of the gradient used for the theme.
- #8B72EE - Purple was the last shade of the gradient used for the theme.

<div align="center">
<img src="./static/images/readme/colors.jpg" alt="Main Logo" width="500">
</div>

### **Typography**

For the main title font used within this project, I used a free font named 'Sprayerz', being imported from the font folder within static/. The font I used for the main site body including the navbar was 'Kanit', supplied by Google Fonts. I used 'Anton', a tall thicker font for the page headers, and then 'Archivo Black' for any info displayed.

### **Wireframes**

For this project, I created a number of wireframes for the layout of different pages.

<details>
<summary><b>Desktop Wireframes</b> - (click to expand)</summary>

### Homepage

The homepage will display 9 works at a time with pagination at the bottom of the screen. At the top there will be a search bar, Add Work button, and a filter sort by button.

<div align="center">
<img src="static\images\readme\wireframes\homepage-d.jpg" alt="Wireframe 1" width="500">
</div>

### Artists Page

The artists page will show all artist names in a grid with 4 names per row. Clicking on these will take the user to the artist page. At the top there will be an Add Artist button.

<div align="center">
<img src="static\images\readme\wireframes\artists-page.jpg" alt="Wireframe 2" width="500">
</div>

### Crews Page

The crews page will show a main crew image larger than images on the works page. This was done to break up the layout of the site. Below this mage will be the crew name. There will also be an Add Crew page.

<div align="center">
<img src="static\images\readme\wireframes\crews.jpg" alt="Wireframe 3" width="500">
</div>

### Styles or Types Pages

Both the Styles and Types pages will have the same layout. Below the image there will be the name of the style or type.

<div align="center">
<img src="static\images\readme\wireframes\styles-types.jpg" alt="Wireframe 4" width="500">
</div>

### View Work Page

When a user clicks on a work, they will be shown the image in large format. Below the image all the info will be shown, allowing users to click onone of these to be taken to its unique page.

<div align="center">
<img src="static\images\readme\wireframes\view-content-d.jpg" alt="Wireframe 1" width="500">
</div>

### View Artist Page

Viewing an artist displays the crews they are affiliated with. Below this all of their works will be displayed.

<div align="center">
<img src="static\images\readme\wireframes\view-artist-page.jpg" alt="Wireframe 1" width="500">
</div>

### View Crew Page

The view crew page is laid out differently once again by showing the main crew image at the top in large size. Below this are all works listed with the crew as main artist, and then each of the crew members are listed. Styles and Types are laid out in the same way without the crew members section at the bottom.

<div align="center">
<img src="static\images\readme\wireframes\crew-page.jpg" alt="Wireframe 1" width="500">
</div>

### Add or Edit Work Pages

To add a work to the database, users will be presented a page will multiple dropdown menus and text boxes. The artist name dropdown will be taking options from the Artists collection. The style dropdown will be taking options from the Styles collection, and the types dropdown will be taking options from the Types collection. Users can then input a year painted and finally an image URL. When editing a work, these fields will be autofilled with the current data binded to that object.

<div align="center">
<img src="static\images\readme\wireframes\add-edit-work.jpg" alt="Wireframe 1" width="500">
</div>

### Add/Edit Artist or Crew or Style or Type Pages

To add either an Artist, Crew, Style or Type to the database, users will be presented with similarly laid out pages. There will be text boxes for names and image URL's to be added. When editing, these fields will be autofilled with the current data binded to that object.

<div align="center">
<img src="static\images\readme\wireframes\add-artist-crew-style-type.jpg" alt="Wireframe 1" width="500">
</div>

### Register Page

The register page will allow users to create a username and password. There is also a confirm password box used to confirm users are aware of their entered password.

<div align="center">
<img src="static\images\readme\wireframes\register.jpg" alt="Wireframe 1" width="500">
</div>

### Login Page

The login page is much like the register page, without the confirm password box.

<div align="center">
<img src="static\images\readme\wireframes\login.jpg" alt="Wireframe 1" width="500">
</div>

### Profile Page

When a user first logs in, they will be redirected to their profile page. This page allows users to view their uploaded content and/or delete their account entirely. At the top of the page is a Delete Account button, followed by an Uploaded Works section, Uploaded Artists section, and an Uploaded Crews section.

<div align="center">
<img src="static\images\readme\wireframes\profile.jpg" alt="Wireframe 1" width="500">
</div>

</details>

<details>
<summary><b>Mobile Wireframes</b> - (click to expand)</summary>

### Large Mobile Responsive Content

Content loaded on large mobile devices will be displayed in rows of 2 items.

<div align="center">
<img src="static\images\readme\wireframes\large-mobile.jpg" alt="Wireframe 1" width="300">
</div>

### Small Mobile Responsive Content

Content loaded on smaller mobile devices will display images in full width mode. This allows users to view the images properly when on smaller screens.

<div align="center">
<img src="static\images\readme\wireframes\small-mobile.jpg" alt="Wireframe 1" width="300">
</div>

### Mobile View Content

When an item is clicked, a page is loaded allowing the user to see the image in full width with all info displayed below.

<div align="center">
<img src="static\images\readme\wireframes\mobile-view-content.jpg" alt="Wireframe 1" width="300">
</div>

### Mobile Multi Content

When viewping pages such as the profile page on mobile, content is displayed in rows of 2 with headers splitting up the sections.

<div align="center">
<img src="static\images\readme\wireframes\mobile-multi-content.jpg" alt="Wireframe 1" width="300">
</div>

</details>

### **Database Architechture**

<div align="center">
<img src="static\images\readme\erd.jpg" alt="Database Architecture" width="600">
</div>

### **Project Management**

This project was designed using an agile approach, utilisng a Kanban board to track my development progress throughout the build. You can view the board I created using Trello [here](https://trello.com/b/mH8fpkjQ/milestone-project-3).

[Back to Table Of Contents](#table-of-contents)

---

## 2 Features

### 2.1 Existing Features

### **Intro Index Landing Page**

When users visit the sites main index page ***(/)***, they are taken to a landing page displaying information about the sites main purpose and how to contribute. From this page, users can either click an Enter button, or can use the navbar to move through the site further.

### **All Works Main Home Page**

This page acts as the home page, displaying all available works uploaded to the database. At the top, users are able to search works according to the artist/crew name, style or type. Users are also able to filter results and order them in several different ways by clicking the Order By dropdown button in the top right. Each work is rendered as a medium sized image panel, which displays information for the work when hovered.

### **Register & Login Pages**

These pages display the logo with a form below allowing users to enter both a username and password. They allow users to either create a new account or login to an existing one by entering these unique values. The application will run validation and authentication on passwords and usernames for character and invalid or existing data checks. 

### **Profile Page**

When a user logs into their account, they will be directed to their own profile page. This will display their name, as well as any content that have contributed to the site in a concise manner. They will also have the option to edit/delete their account or any personally created content.

### **Logout**

The logout route link is displayed in the top right corner of the navbar when users are logged into an account. Clicking logout will remove 'user' from session cookies, effectively logging them out.

### **New Upload Page**

This page allows users to upload a new work to the database. It allows users to first select whether the work is by an artist or crew, as this will modify the content accordingly. Users can then select from a list of existing Artists or Crews respectively, before selecting the applicable Style and Type of the work, as well as the year painted and image URL. Each of these inputs either take data directly from certain collections within the database, or allow users to input their own values with respective validation applied. All submitted data is then saved in the works collection and displayed on the site accordingly.

### **Work Page**

When a user clicks on a work, they will be taken to a dedicated page allowing them to view the image in full size without any clipping. This page also displays the information relating to the work object:- Artst, Style, Type, and Year Painted. If the user uploaded the work or is the admin, they will be shown buttons at the very bottom allowing them to edit or delete the object.

### **Edit Work Page**

A work can be edited via the Edit Work page if the data assigned to the work object needs to be updated. A particular user only has access to edit a work if they were the one to originally upload it to the database. The admin can edit any work object.

### **Add Artist Page**

Users can easily add artists to the database by navigating to this page and inputting an artist name, their respective crews, and submitting. Validation will check for character input as well as existing data in the Artists collection.

### **Artists page**

The Artists page displays all artists uploaded to the database. Clicking on any of these will take the user to the artist dedicated page. There is also an 'Add Artist' button that will direct users to that page if they are logged in.

### **Artist Page**

Upon clicking an artists name, they will be taken to the artists individual page. This will display any information pertaining to the selected artist object, including any crew associations that artist may have, along with all works in their name. Please note when clicking on the artist name on a crew work, users will be taken to the crew page instead. If the user uploaded the artist or is the admin, they will be shown buttons at the very bottom allowing them to edit or delete the object.

### **Edit Artist Page**

An artist can be edited via the Edit Artist page if the data assigned to the artist object needs to be updated. A particular user only has access to edit an artist if they were the one to originally upload them to the database. The admin can edit any artist object.

### **Add Crew Page**

Users are able to add new crews to the database by navigating to this page and inputting the crew name and image. Validation will check for character input as well as existing data in the Crews collection.

### **Crews Page**

The Crews page displays all crews uploaded to the database, along with their main crew image. They are displayed in large card panels, breaking up the layout of the site and allowing the user to see the crew image clearly. Clicking one of these crew panels takes the user to the individual Crew page.

### **Crew Page**

The Crew page shows all associated data for the selected crew object. Underneath the crew image, each artist associated with the crew is displayed. Below this, each work with the crew listed as the main artist is also displayed. Clicking either an artist name or work will redirect the user to its respective page. If the user uploaded the crew or is the admin, they will be shown buttons at the very bottom allowing them to edit or delete the object.

### **Edit Crew Page**

A crew can be edited via the Edit Crew page if the data assigned to the crew object needs to be updated. A particular user only has access to edit a crew if they were the one to originally upload it to the database. The admin can edit any crew object.

### **Add Style Page [Admin Only]**

The admin is able to add new styles to the database by navigating to this page and inputting the style name and image. Only the admin is able to add styles as users should not have a reason to add any styles to the database. Validation will check for character input as well as existing data in the Styles collection.

### **Styles Page**

The Styles page displays all of the different styles of graffiti. Users can upload works and correctly categorise them under a respective styles. These are also displayed in large card panels, further breaking up the layout of the site and allowing the user to see the style image clearly. Clicking one of these style panels takes the user to the individual Style page.

### **Style Page**

The Style page shows all associated data for the selected style object. Underneath the style image, each work executed and categorised within this style is displayed. Clicking any of these works will redirect the user to its respective page. The admin will be shown buttons at the very bottom allowing them to edit or delete the object.

### **Edit Style Page [Admin Only]**

A style can be edited by the admin via the Edit Style page. No normal users are allowed to do this.

### **Add Type Page [Admin Only]**

The admin is able to add new types to the database by navigating to this page and inputting the type name and image. Validation will check for character input as well as existing data in the Types collection.

### **Types Page**

The Types page displays all of the different types of graffiti there can be. Users can upload works and correctly categorise them under their respective type, for example an individual work can be by the same artist in the same style, but may be on a freight train as apposed to on a legal wall. Each type is also displayed in large card panels, further breaking up the layout of the site and allowing the user to see the type image clearly. Clicking one of these type panels takes the user to the individual Type page.

### **Type Page**

The Type page shows all associated data for the selected type object. Underneath the type image, each work executed and categorised of this type is displayed. Clicking any of these works will redirect the user to its respective page. The admin will be shown buttons at the very bottom allowing them to edit or delete the object.

### **Edit Type Page [Admin Only]**

A type can be edited by the admin via the Edit Type page. No normal users are allowed to do this.

### **Admin Panel Page [Admin Only]**

The admin panel facilitates the ability for the site administrator to easily delete any user in the database if they violate the correct use of the website. The page also displays buttons allowing for Styles or Types to be added to the database. All other content edit/delete admin privileges did not need to be included here as they are accessible across the site when logged into the admin account.

### **Header**

Each page contains the header which has a background image filling the entire width of the screen and extending down from the top of the window 300px in height. At the top sits the navbar and in the center of the header there is a black bordered box used as the title logo containing the text Bristol Blackbook. This box has a gradient border fading from white to black, and the text is underlined with a gradient matching the purple colour scheme for the entire site. The bottom of the header background image also has a gradient fading to black, allowing the image to blend with the body background effectively. 

### **Navbar**

Due to the header, each page across the application naturally also contains the full width navbar at the very top of the window, facilitating effortless navigation across the site. This navbar sits at the very top of the header and has a black background with 70% opacity, allowing for the header image to be seen behind. The main logo is displayed in the far left, followed by page links for Home, Artists, Crews, Styles and Types, and on the far right sits the Login and Register page links. The content of the navbar changes when users are logged into an account. On the left additional links of New Upload, Add Artist and Add Crew are displayed, and the far right links are both entirely swapped to display the Profile and Logout route links.

### **Footer**

Each page has a full width footer at the bottom of the window, containing social media links and copyright information.

### **404 Error Handling Page**

In case a user encounters a 404 error, 

### 2.1 Features Left To Implement

### **Bristol Paint Shops Page**

I want to create a page that lists each of the shops in Bristol that sell decent spray paint. I will include their name, location, and opening times, as well as any known deals available, ontop of listing the general price range for each brand stocked.

### **Work Rating System**

The ability for users to grade each work on a 5 star rating system would ultimately grant the site owner a deeper level of insight into the users of their site. This would allow not only the site owner to have additional data on its audience, but other users will benefit from this feature as it will display the opinion and feedback of other fellow site users. Perhaps the most important aspect of this feature however is that the original uploader or even artist can benefit from these types of statistics by seeing the direct user rating of each created work.

### **Comments Section On Works**

Originally Disqus was used as a comment secion, however it was removed as I would like to create my own comments section in the future. This will allow site users to comment on content under their own usernames with their created account without any additional registration as seen with Disqus.

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

### [**Flash_Paginate**]()

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
    - os.environ.setdefault("DEBUG", "FALSE")

- Then create a ***.gitignore*** file, and include this env.py file inside it to ensure your environment variables are never published publically by being pushing to GitHub.

- You are now ready run this project and push any modifications to your own repository. To run, type into the terminal ***python app.py***.

To read more about cloning repositories, you can read [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to Table Of Contents](#table-of-contents)

## 6 Credits

### 6.1 Content and code

Pagination - https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9

### 6.2 Media

### 6.3 Acknowledgements

### 6.4 References

[Back to Table Of Contents](#table-of-contents)