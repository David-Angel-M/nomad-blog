# Nomads Travel Blog

## 1. Definition Problem
The main idea is to design and create a travel blog web application that allows adventurers to document and share theirs trips and personal stories with other community members, with the intent to get useful and resourceful information from each other’s personal experiences. Users must be registered and logged-in to be able to post trips on the site. Once logged-in, the users should be able to create, edit, and delete their own posts. Additionally, the application should allow all users, regardless of login status, to view and comment  all the existing content on the site.

## 2. Project Goal
Create a Full-Stack Web Application where travelers can share their journeys, insights and recommendations, as well as leave helpful comments on the published content. The purpose is to create an interactive and resourceful community through everyone’s interactions and feedback, members and visitors alike. The platform should prioritize easy navigation and must be responsive across various devices.

## 3. Technologies I've used
- Python was used to write the functions and models as needed by the business logic.
- Balsamiq was used to create the wireframes during the design process.
- Django is the framework used to create the project and app’s functionality following the MVT  design pattern guideline ( Models, Views, Templates).
- Pep8 was used for formatting and error-checking Python code.
- GitHub repository was used to store the project's code.
- PostgreSQL was used as the relational database.
- Cloudinary was used to store static files, media and style files
- Responsive CSS was implemented using Bootstrap 5.
- Google fonts were used to add fonts for aesthetic and UX purposes
- Crispyforms were used to display forms.


## 4. Database Design
This is the Relational Database used to create the models for the web application. [Database schema](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/3_DB_Schema.jpg)

## 5. Agile Methodology
All functionality and development of this project was managed using [Trello](https://trello.com/b/bjGo9ZMY/nomad-blog)

## 6. User stories
###  6.1 Register
As a site user, I want to be able to register on the application in order to publish or update posts. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_1_Register.png)

###  6.2 Login
As a As a site register user, I want to be able to log in to the application in order to publish or update posts. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_2_Login.png)

###  6.3 Home
As a site user, I want to be able to log in to the application in order to publish or update posts. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_3_Home.png)

###  6.4 Filter Category for Non-Logged-in Users
As a site user, I want the ability to filter posts based on different categories.
[Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_4_FIlter%20Category.png)

###  6.5 Comments for Non-Logged-in Users
As a site user, I want the ability to leave comments on each post. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_5_Comments.png)

###  6.6 Post List for Logged-in Users
As a site user, I want to be able to view the posts that I create for update or view the post. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_6_Post%20List%20for%20Logged-in.png)

### 6.7 Create Post
As a site user, I want to be able to create a post to publish on the blog. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_7_Create%20Post.png)

### 6.8 Update Post
As a site user, I want to be able to edit a post and make changes to its fields.
[Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_8_UpdatePost.png)

### 6.9 Delete Post
As a site user, I want to be able to delete a post so that it no longer appears on the blog. [Wireframe](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/6_9_Delete%20Confirm.png)

## 7. Design Structure
### 7.1 Font
Google font Lato was chosen with to be used across the entire site.

### 7.2 Colors
| Use           | Hex     | Color                                                    |
| ------------- | ------- | -------------------------------------------------------- |
| Background    | #f8f9fa | ![#f8f9fa](https://via.placeholder.com/10/f8f9fa?text=+) |
| Cards         | #fff    | ![#fff](https://via.placeholder.com/10/fff?text=+)       |
| NavBar        | #343a40 | ![#343a40](https://via.placeholder.com/10/343a40?text=+) |
| Footer        | #424649 | ![#424649](https://via.placeholder.com/10/424649?text=+) |
| Btn Primary   | #6c757d | ![#6c757d](https://via.placeholder.com/10/6c757d?text=+) |
| Inputs        | #ccc    | ![#ccc](https://via.placeholder.com/10/ccc?text=+)       |

### 7.3 Navigation
- A Navbar was created on top of the page for easy user navigation through the web app.
- Add, Edit/Update are straightforward forms that allow users the use the features with ease.

## 8. Results
[Link to the project](https://nomad-travel-blog-caffc3139c3a.herokuapp.com/)

###  8.1 [Register](https://nomad-travel-blog-caffc3139c3a.herokuapp.com/register)

###  8.2 [Login](https://nomad-travel-blog-caffc3139c3a.herokuapp.com/login)

###  8.3 [Main Page](https://nomad-travel-blog-caffc3139c3a.herokuapp.com/)

###  8.4 [Post List for Logged-in Users](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/8_4_Login_List.JPG)

###  8.5 [Filter Category for Non-Logged-in Users](https://nomad-travel-blog-caffc3139c3a.herokuapp.com/category/1/)

###  8.6 [Comments for Non-Logged-in Users](https://nomad-travel-blog-caffc3139c3a.herokuapp.com/post-detail/6/comment/)

### 8.7 [Create Post](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/8_7_PostCreate.JPG)

### 8.8 [Update Post](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/8_8_UpdatePost.JPG)

### 8.9 [Delete Post](https://github.com/David-Angel-M/nomad-blog/blob/main/doc/8_9_DeletePost.JPG)

## 9. Testing
### 9.1 Lighthouse report
- Home page [Result]()
- Login page [Result]()

### 9.2 WAVE Webaim Accessibility testing
The WAVE tool was used to test all pages on the app. Due to empty social links some common errors were found repeatedly over each tested page,  those were:

- Home page WAVE [Result](https://wave.webaim.org/report#/https://nomad-travel-blog-caffc3139c3a.herokuapp.com/)
- Login page WAVE [Result](https://wave.webaim.org/report#/https://nomad-travel-blog-caffc3139c3a.herokuapp.com/login)
- Register page WAVE [Result](https://wave.webaim.org/report#/https://nomad-travel-blog-caffc3139c3a.herokuapp.com/register)

### 9.3 CSS Validator results
I use https://jigsaw.w3.org/css-validator/validator.html.en option Validate by direct input the style.css. [Result]()

### 9.4 HTML Validation
I use https://validator.w3.org/ option Validate by URI to test html. [Result]()

### 9.5 Manual Testing
During the manual testing phase, I examined the user inputs and functionality of the website. My objective was to compare the feedback and results obtained from testing against the expected outcomes. Any unexpected outputs or outcomes encountered were promptly addressed and resolved.

#### Desktop Testing:
I thoroughly tested all aspects of the site on Chrome and Safari browser, and I am pleased to report that everything functions flawlessly. Pages load swiftly, and all features, including CRUD operations, user authentication (login/logout), register process, trips addition, and category filter work without any issues.

#### Mobile Testing:
I conducted a thorough testing on three different mobile devices: Apple iPhone 11, Samsung S20FE, and Samsung S7 tablet. The website showcased excellent responsiveness and adaptability across various devices. The site performed seamlessly on Apple's Safari browser as well.

## 10. Features left to implement
I would like to: 
-	Add a search bar to find travel posts
-	Include a user profile page allowing users to edit, or delete their profile
-	Add more fields to the blog like most likes

## 11. Deployment
The site was deployed using Heroku, by following the steps found in the tutorials and guidelines of CodeInstitute’s material:
- Using my Heroku account
- Create a new app whilst logged in
- Connect my GitHub repository via "Connect to GitHub" option in Heroku
- Set up the config vars for the project.
- Enable either "Automatic Deploy"

## 12. Credits and references
- Stackoverflow.
- Student Care.
- Slack Community.
- W3Schools.
- Family and Friends.
- Travel blog images was taken from https://unsplash.com/

## 13. Acknowledgements
This Travel Blog was created for my PP4 Project for the Full Stack Developer program with Code Institute.

DAVID ANGEL, 2022/2023
