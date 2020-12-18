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
  - [**1.3 User Stories**](#13-user-stories)
  - [**1.4 Design Process**](#14-design-process)

- [**2 Features**](#2-features)

  - [**2.1 Existing Features**](#21-existing-features)
  - [**2.2 Features Left to Implement**](#22-Features-left-to-impliment)

- [**3 Technologies Used**](#3-technologies-used)
  - [**3.1 Languages**](#31-languages)
  - [**3.2 Frameworks & Libraries**](#32-frameworks-&-libraries)
  - [**3.3 Tools**](#33-Tools)

* [**4 Testing**](#4-testing)
  - [**4.1 Completed**](#41-completed)
  - [**4.2 Bugs**](#42-bugs)

* [**5 Deployment**](#5-deployment)

  - [**5.1 Heroku**](#51-github-pages)
  - [**5.2 Locally**](#52-locally)

* [**6 Credits**](#6-credits)
  - [**6.1 Contents and code**](#61Contents-and-code)
  - [**6.2 Media**](#62-media)
  - [**6.3 Acknowledgements**](#63-Acknowledgements)

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
- As a user, I want to be able to easily browse all individual artists, crews, styles and types in the db.
- As a user, I want to register for an account so that I can contribute to the database.
- As a user, I want to see how to add content, so that I can easily contribute to the database.

### Returning/Registered Users

- As a registered user, I want full CRUD functionality.
- As a returning user, I want to log into my account and be presented with my own profile page.
As a returning user, I want to see what I have uploaded to the database, so that I can track my contributions.
- As a returning user, I want control over my data, so that I can easily choose to delete the account or any content I have uploaded to the website.

### Site Owner

- As the site owner, I want users to register for accounts so that I can implement authentication.
- As the site owner, I want users to register for accounts so that I can personalise their experience.
- As the site owner, I want access to all features available to the site when logged in as admin.
- As the site owner, I want to be able to see all users registered to the site so that I can track who has registered and delete any accounts if needed.

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
- #FFFFFF - White was used for the main body text color.
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

When a user clicks on a work, they will be shown the image in large format. Below the image all the info will be shown, allowing users to click on one of these to be taken to its unique page.

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

To add a work to the database, users will be presented a page will multiple dropdown menus and text boxes. The artist name dropdown will be taking options from the Artists collection. The style dropdown will be taking options from the Styles collection, and the types dropdown will be taking options from the Types collection. Users can then input a year painted and finally an image URL. When editing a work, these fields will be autofilled with the current data bound to that object.

<div align="center">
<img src="static\images\readme\wireframes\add-edit-work.jpg" alt="Wireframe 1" width="500">
</div>

### Add/Edit Artist or Crew or Style or Type Pages

To add either an Artist, Crew, Style or Type to the database, users will be presented with similarly laid out pages. There will be text boxes for names and image URL's to be added. When editing, these fields will be autofilled with the current data bound to that object.

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

When viewing pages such as the profile page on mobile, content is displayed in rows of 2 with headers splitting up the sections.

<div align="center">
<img src="static\images\readme\wireframes\mobile-multi-content.jpg" alt="Wireframe 1" width="300">
</div>

</details>

### **Database Architechture**

The diagram below outlines the structure and arcitecture of my database. Each seperate entity corresponds to a collection within my database. The population of entity parameters by other entity parameters is clearly displayed using arrows. These relational populations are either automatic or require the user to select from a list of values fed from the other collection.

Within MongoDB, I only had to create the empty collections - all data was entered and created on the frontend of the website.

<div align="center">
<img src="static\images\readme\erd.jpg" alt="Database Architecture" width="600">
</div>

### **Project Management**

This project was designed using an agile approach, utilising a Kanban board to track my development progress throughout the build. You can view the board I created using Trello [here](https://trello.com/b/mH8fpkjQ/milestone-project-3).

[Back to Table Of Contents](#table-of-contents)

---

## 2 Features

### 2.1 Existing Features

### **Intro Index Landing Page**

When users visit the sites main index page ***(/)***, they are taken to a landing page displaying information about the sites main purpose and how to contribute. From this page, users can either click an Enter button, or can use the navbar to move through the site further.

### **All Works Main Home Page**

This page acts as the home page, displaying all available works uploaded to the database. The page displays 9 works per page, pagination pages and links are clearly visible at the bottom of the images panels. At the top, users are able to search works according to the artist name. Users are also able to filter results and order them in several different ways by clicking the Order By dropdown button in the top right. Each work is rendered as a medium sized image panel, which displays information for the work when hovered.

### **Register & Login Pages**

These pages display the logo with a form below allowing users to enter both a username and password. They allow users to either create a new account or login to an existing one by entering these unique values. Registration requires the user to enter their password twice. The application will run validation and authentication on passwords and usernames for character and invalid or existing data checks.

### **Profile Page**

When a user logs into their account, they will be directed to their own profile page. This will display their name, as well as any content that have contributed to the site in a concise manner. They will also have the option to delete their account or any personally created content.

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

Due to the header, each page across the application naturally also contains the full width navbar at the very top of the window, facilitating effortless navigation across the site. This navbar sits at the very top of the header and has a black background with 70% opacity, allowing for the header image to be seen behind. The main logo is displayed in the far left, followed by page links for Home, Artists, Crews, Styles and Types, and on the far right sits the Login and Register page links. The content of the navbar changes when users are logged into an account. On the left additional links of New Upload, Add Artist and Add Crew are displayed, and the far right links are both entirely swapped to display the Profile and Logout route links. The navbar is also responsive, switching to a collapsable hamburger type menu on tablet and mobile devices. This works well due to the length of the links when logged in.

### **Footer**

Each page has a full width footer at the bottom of the window, containing social media links and copyright information.

### **404 & 500 Error Handling Page**

In case a user encounters a 404 or 500 error, they will be redirected to this page. It explains there was an issue and allows users to click to go back home.

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

### [**PyMongo**](https://pypi.org/project/pymongo/)

PyMongo is a distribution of Python used to interact with the MongoDB database.

### [**Flask-paginate 0.7.1**](https://pypi.org/project/flask-paginate/)

This was used to paginate the works on the main works page.

### [**BSON ObjectID**](https://docs.mongodb.com/manual/reference/method/ObjectId/)

This was used to create and parse ObjectID's from the MongoDB database.

### [**MD Bootstrap 4.19.1**](https://mdbootstrap.com/)

Material Design Bootstrap is a free open source CSS framework, combining styles from Material Design with the main functionality of Bootsptrap. I used MDB to fill the site with boilerplate content when building the functionality, but it was also used to create responsiveness.

### [**Font Awesome**](https://fontawesome.com/)

Font Awesome 5.8.2 was used for icons across the site.

### [**Google Fonts API**](https://fonts.google.com/)

Most of the fonts used within this project were provided by the Google Fonts API. The fonts used were 'Anton' 'Kanit', and 'Archivo Black'.

### 3.3 Tools

### [**MongoDB Atlas**](https://www.mongodb.com/cloud/atlas)

Atlas is the cloud hosted version of MongoDB's database service. This was used as my database for the project.

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

Used to create the wireframes for this project.

### [**Lucid**](https://lucid.app/)

Used to create the entity relationship diagram for this project.

[Back to Table Of Contents](#table-of-contents)

---

## 4 Testing

### 4.1 Completed

### **Automated Testing**

- DevTools Lighthouse - I ran extensive testing with the lighthouse tool. Any pages that did not return green 90+ scores in each area were worked on to solve issues that could be addressed. Some issues included image sizes and redundant code in Bootstrap files.

- [HTML Validator](https://validator.w3.org/) - All code passed except for a few duplicate IDs and warnings on external code. I was able to discover and fix a duplicate anchor link bug using this validator.

- [CSS Validator](https://jigsaw.w3.org/) - All code passes this validator with no errors. Only warnings on external code from MDB. 

- [JavaScript Validator](jshint.com) - All code passed with no errors.

- [Python PEP8 Validator](http://pep8online.com/) - Most of my code was python based. I ran my code through the PEP8 validator and made sure no issues were raised.

<div align="center">
    <img src="./static/images/testing/pep8.jpg" alt="PEP8" width="700">
</div>

### **Manual Testing**

In place of unit testing my code, I manually tested that all site features and routes work as expected without error. Through the following tests, I demonstrate that the application has full CRUD functionality available from the frontend.

<details>
<summary><b>Checking User Stories</b> - (click to expand)</summary>

### First Time Users

- As a user, I want a site to have a clearly defined purpose when I first enter so that I know what I am viewing.
    - The main landing page describes exactly what the site is for. - PASS

- As a user, I want to register for an account so that I can contribute to the database.
    - The Register button is clearly displayed on the navbar. - PASS
    - Registration functionality works, as demonstrated below. - PASS

- As a user, I want to be able to browse all works in the db.
    - The home page from the navbar displays all works uploaded to the db. - PASS

- As a user, I want to clearly see the artist name, style, type and year painted for each work.
    - When hovering the mouse over an image thumbnail on the main works page, all info is diaplayed. - PASS
    - If an image is clicked, a dedicated page containing the image in large scale along with all info is returned. - PASS

- As a user, I want to be able to easily browse all individual artists, crews, styles and types in the db.
    - The navbar displays links to pages displaying each of these items. - PASS
    - Each page lists all of the items within the db clearly. - PASS

- As a user, I want to see how to add content, so that I can easily contribute to the database.
    - Each page has a button to add an item of that sort to the database. - PASS
    - Users logged in will see these links on the navbar. - PASS

- As a user, I want all functionality on the site to work to avoid a bad experience.
    - All functionality works as expected. Please see further testing below. - PASS


### Returning/Registered Users

- As a registered user, I want full CRUD functionality.
  - Users are able to Create their own data, Read all data, Update and Delete their own data. Only the Read functionality is available to non registered users. - PASS

- As a returning user, I want to log into my account and be presented with my own profile page for a personalised experience.
  - Users are automatically redirected to their profile page when they log in. - PASS

- As a returning user, I want to see what I have uploaded to the database, so that I can track my contributions.
    - When users sign in, they are shown their profile page. This shows a concise list of all their uploaded contributions. - PASS

- As a registered user, I want control over my data, so that I can easily choose to delete the account or any content I have uploaded to the website.
    - The option to delete a users account is displayed on their user panel. - PASS
    - All items they have uploaded will display buttons allowing them to edit/delete it. - PASS

### Site Owner

- As the site owner, I want users to register for accounts so that I can implement authentication.
  - Users are able to register for an account easily. - PASS
  - User authentication applied and tested sucessfully. - PASS

- As the site owner, I want users to register for accounts so that I can personalise their experience.
  - Users are given their own profile page. This displays their name and uploaded content. - PASS
  - Navbar links will change for users visiting vs logged in. - PASS

- As the site owner, I want access to all features available to the site when logged in as admin.
  - The admin account has access to all features site wide. - PASS
  - The admin has full CRUD functionality over all data on the site. - PASS
  - The admin panel displays all users registered, as well as buttons to pages normal users cannot access. - PASS

- As the site owner, I want to be able to see all users registered to the site so that I can track who has registered and delete any accounts if needed.
  - The admin panel displays all users registered, there is a Delete button below each user account name shown. - PASS

</details>

<details>
<summary><b>Testing Functionality</b> - (click to expand)</summary>

### Navbar

- Each navbar link tested and working from each page. - PASS
- The main logo takes the user to the welcome page. - PASS
- Viewing the website on tablet or mobile devices, the navbar links dissapear and a hanmburger icon appears instead. Clicking this shows a drop down menu with all links.  - PASS

### Buttons

- The main header takes the user to the welcome page. - PASS

- The ENTER button on the welcome page returns the /works page with a 200 status code. - PASS

- All Add buttons - When users are not signed in, they get redirected to the login page with a 302 status code. When users are signed in, they are taken to the correct page with a 200 status code, as long as the page is not admin only. - PASS

- All Go Back buttons return 200 codes to the correct page. - PASS

- Both Artist and Crew Upload buttons display or hide one another when pressed, keeping only one on the screen at any one time. - PASS

- All form submit buttons POST data sucessfully. - PASS

- All Edit/Delete buttons correctly modify their data. - PASS (One bug has been found and is noted under bugs.)

### Links

- All social media links redirect to the correct websites. - PASS

- External links correctly open in a new tab using target='_blank'. - PASS

- Clicking any image takes the user to that images page. From here, clicking the artist name, style or type will take the user to each respective page. All info links work correctly as expected. - PASS

- Clicking a crew name or artist name takes the user to the individual pages, where more detail about the object is correctly displayed. - PASS

No links are broken. - PASS

### Forms

- All forms were tested for prompting incorrect input types. - PASS

- All correct validation working and displaying. - PASS

- Character count limitations working. - PASS

- When posting a form with empty data, the form validation prompts the user that they must enter a value. - PASS

### Responsiveness

- All pages respond to different screen sizes effectively. - PASS

- No content behaves weirdly when resized and correctly repositions. - PASS

- No content overflows off the page at any size. - PASS

</details>

<details>
<summary><b>Testing 200 Codes</b> - (click to expand)</summary>

### All Users Pages

- /welcome - PASS
- /login - PASS
- /register - PASS
- /works - PASS
- /artists - PASS
- /crews - PASS
- /styles - PASS
- /types - PASS

<div align="center">
    <img src="./static/images/testing/main-pages-200.jpg" alt="PEP8" width="700">
</div>

- /work/ObjectID - PASS
- /artist/artist_name - PASS
- /crew/crew_name - PASS
- /style/style_name - PASS
- /type/type_name - PASS

<div align="center">
    <img src="./static/images/testing/get-pages-200.jpg" alt="PEP8" width="700">
</div>

### Registered User Pages

- /profile/username - PASS
- /new_work - PASS
- /add_artist - PASS
- /add_crew - PASS
- /add_style - PASS
- /add_type - PASS

<div align="center">
    <img src="./static/images/testing/add-pages-200.jpg" alt="PEP8" width="700">
</div>

- /edit_work/ObjectID - PASS
- /edit_artist/artist_name - PASS
- /edit_crew/crew_name - PASS
- /edit_style/style_name - PASS
- /edit_type/type_name - PASS

<div align="center">
    <img src="./static/images/testing/edit-pages-200.jpg" alt="PEP8" width="700">
</div>

- I tested the pagination, checking the correct query parameter was passed for each page. - PASS

<div align="center">
    <img src="./static/images/testing/get-works-pagination.jpg" alt="PEP8" width="700">
</div>

</details>

<details>
<summary><b>Testing 302 Codes</b> - (click to expand)</summary>

### Visitor Page Redirects

When a user is not logged into an account, they are unable to access any pages beyond the standard Read level functionality and will be redirected to the login page. - PASS

<div align="center">
    <img src="./static/images/testing/redirects-302.jpg" alt="PEP8" width="700">
</div>

### Admin Only Pages

Logging in with the username 'test', I tried to access add_type and add_style pages that only the admin should have access to. - PASS

<div align="center">
    <img src="./static/images/testing/admin-pages-302.jpg" alt="PEP8" width="700">
</div>

</details>

<details>
<summary><b>Testing User Scenarios & CRUD Functionality</b> - (click to expand)</summary>

### Registering An Account - PASS

- Clicking on the Register page link.
- Entering 'TestName' as a username.
- Entering 'TestPassword' as a password.
- Confirming this password.
- Check for profile redirect and flash displaying username.

<div align="center">
    <img src="./static/images/testing/creating-test-profile.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/testname-register-302.jpg" alt="PEP8" width="700">
</div>

### Creating A Crew - PASS

- Clicking on the Crews page.
- Clicking the Add Crew button.
- Entering 'Team123' as the crew name.
- Entering an image as the crew photo.
- Submitting the form.
- Check for page redirect and flash displaying success.
- Find crew and click on it to view.

<div align="center">
    <img src="./static/images/testing/create-crew.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/create-crew.jpg" alt="PEP8" width="700">
</div>

### Creating An Artist - PASS

- Clicking on Artists page.
- Clicking the Add Artist button.
- Entering 'MrTee' as the artist name.
- Assigning the artist to the 'Team123' crew previously created.
- Submitting the form.
- Check for page redirect and flash displaying success.
- Find artist and click on it to view.

<div align="center">
    <img src="./static/images/testing/create-artist.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/create-artist.jpg" alt="PEP8" width="700">
</div>

### Uploading A New Work - PASS

- Clicking on Works/Home page.
- Clicking the New Work button.
- Entering 'MrTee' as the artist name.
- Assigning the work a stye of 'Dub'.
- Assigning the work a type of 'Legal Spot'
- Entering an image URL for the work.
- Submitting the form.
- Check for page redirect and flash displaying success.
- Find work at top of main page and click on it to view.

<div align="center">
    <img src="./static/images/testing/create-work.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/new-work.jpg" alt="PEP8" width="700">
</div>

### Edit or Delete Work - PASS

- Clicking on the work to edit/delete.
- Clicking the Edit button at the bottom of the page.
- Checking all of the fields are prefilled with the objects data.
- Clicking Cancel to be returned to the Works page.
- Clicking on the work again.
- Clicking the Delete button at the bottom of the page.
- Clicking Yes on the modal popup.
- Check for page redirect and flash displaying successful delete.
- Check that the work is now gone from All Works.

<div align="center">
    <img src="./static/images/testing/edit-delete-work.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/edit-delete-work.jpg" alt="PEP8" width="700">
</div>

### Logout and Login - PASS

- Clicking on the Logout link on the navbar.
- Checking for page redirect and flash displaying logout success.
- Checking the navbar links have changed now user is not logged in.
- Page was redirected to Login page, so entering 'TestName' as username.
- Entering 'TestPassword' as password.
- Clicking Login button.
- Checking for page redirect to user profile and flash displaying login success.

<div align="center">
    <img src="./static/images/testing/logout-login.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/logout-login.jpg" alt="PEP8" width="700">
</div>

### Delete Content and Account - PASS

- Clicking on the profile page link on the navbar.
- Deleting any uploaded content on the test account.
- Returning to profile page when all content is removed.
- Clicking Delete Account and Yes on modal pop up.
- Checking for page redirect to main works page with flash displaying deletion success.
- Checking the navbar links have changed as user is no longer logged in.

<div align="center">
    <img src="./static/images/testing/delete-artist-then-account.gif" alt="PEP8" width="700">
</div>

<div align="center">
    <img src="./static/images/testing/delete-artist-then-account.jpg" alt="PEP8" width="700">
</div>

</details>

### 4.2 Bugs

### **Fixed**

- Spelling mistakes in some class and id names were discovered and fixed through testing.

- Delete modals would sometimes delete the wrong object. This was fixed through testing.

- Created onerror image for images that break and cause the site to look bad.

### **Still Existing**

- On the profile page, when users click to delete a work, the modal window glitches out and jumps between the center of the screen and inside the work card panel. This often makes it really hard to click one of the options. This needs to be fixed by repositioning the divs.

- The gradient underline on the header logo box displays strangely on Apple Facebook and Safari browsers. The underline displays as a full box, there may be some code to fix this but due to time this will have to wait.

- The search feature only returns the artist name. All objects used to return if a query matched, so I may have changed the code by accident. I could not see the issue when looking inititaly, so for now the feature just searches for the artist name and this fix can be implemented at a later date.

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

- First open your IDE and navigate to the working directory you want to use.

- You then need to create a ***virtual environment*** to install all dependencies in a sandbox. To do this using venv use the following code:
  - ***python3 -m venv <YOUR_DIR>***

- When your virtual environment is created you need to activate it with the following code:
  - ***<YOUR_DIR>\Scripts\activate***

- Follow this link to the repository for [Bristol Blackbook](https://github.com/samlaubscher/Bristol-Blackbook).

- In the top corner next to the ***About*** section, click the ***Code*** button with the downwards facing arrow icons.

- Under the ***Clone*** section, make sure the HTTPS tab is highlighted, and copy the link displayed to your clipboard. It should look like this:
    > https://github.com/samlaubscher/Bristol-Blackbook.git

- Open ***Git Bash*** in your IDE.

- Then type into the terminal window ***git clone {URL}*** and replace the ***{URL}*** with the link copied from the repository page.

- Upon hitting ***Enter*** the repository will be cloned into your current working directory.

- To then remove the origin link to this repository from your IDE, type ***git remote rm origin***.

- Alternatively, you can download the repository directly as a compressed ZIP folder from the ***Code*** dropdown box, underneath the ***Clone*** section. Unpack this ZIP folder into your virtual environment location.

- When the project is successfully cloned or downloaded and opened in the virtual environment, you need to install any dependancies and requirements by typing ***pip3 install -r requirements.txt*** into your IDE's terminal window.

- You next need to create an ***env.py*** file to store your environment variables. For this project, they are: 
    - import os
    - os.environ.setdefault("IP", "YOUR IP")
    - os.environ.setdefault("PORT", "5000")
    - os.environ.setdefault("SECRET_KEY", "YOURSECRETKEY")
    - os.environ.setdefault("MONGO_URI", "mongodb+srv://root:YOURPASSWORD@YOUR-CLUSTER-NAME.2qobt.mongodb.net/YOUR-DATABASE-NAME?retryWrites=true&w=majority")
    - os.environ.setdefault("MONGO_DBNAME", "YOUR-DATABASE-NAME")
    - os.environ.setdefault("DEBUG", 0)

- Then create a ***.gitignore*** file, and include this env.py file inside it to ensure your environment variables are never published publically by being pushing to GitHub.

- You are now ready run this project and push any modifications to your own repository. To run, type into the terminal ***python app.py***.

To read more about cloning repositories, you can read [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to Table Of Contents](#table-of-contents)

## 6 Credits

### 6.1 Content and code

Code for the preloader was taken from here - https://bootsnipp.com/snippets/GaeVl

Code for the pagination was taken from this guide - https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9

All additional code was my own.

### 6.2 Media

Most images were taken from the internet and are not my own. I asked permission to use most of the images from friends accounts.

### 6.3 Acknowledgements

I would like to thank my mentor Ignatius for the time he has spent with me going over this project. I would also like to thank all students that offered advice, all people who supported me in any way during the project, and all friends that took the time to look at the site during development.

[Back to Table Of Contents](#table-of-contents)