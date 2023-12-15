# COMP-440-Course-Project

For all parts of this project, your system must be desktop or web-based application. You can use
ANY development tools, however, some simple GUI interfaces are required for each functionality.
All functionalities must be performed via the interface of your system; direct SQL statement
execution via any tools (like MySQL Workbench) is not allowed. 

**Part 1 – Deadline: Monday, 10/09 by midnight**
Use Java/C#/PHP/Python/C++ and SQL, implement the following functionality:
1. (5 pts) Create a database schema and implement a user registration and login interface so
that only a registered user can login into the system. The schema of the user table should be:
user(username, password, firstName, lastName, email)
username is the primary key, and email should be unique. You have to prevent the SQL
injection attack. There is an attached pdf file about SQL injection attacks.
2. (5 pts) Sign up for a new user with information such as: username, password, password
confirmed, first name, last name, email. Duplicate username, and email should be detected
and fail the signup. Unmatching passwords should be detected, as well.

**Part 2: Deadline: Monday, 10/30, by midnight**
Based on part 1, implement the following functionality using your selected programing language and
SQL with necessary GUI interfaces. Part 2 emphasizes the programming of interfaces and design and
their integration with database operations.
1. (6.25 pts) Implement a interface so that a user can insert an item, such as:
  Title: Smartphone
  Description: This is the new iPhone X
  Category: electronic, cellphone, apple
  Price: 1000
The IDs of items should be generated automatically using autoincrement feature of MySQL.
Make sure that a user can only post 3 items a day.
2. (6.25 pts) Implement a search interface as a form so that after one type in a category, all the
items with that category are returned. The result needs to be shown as a table/list on a page.
3. (6.25 pts) Select an item from the above list, and one can write a review like the following:
A dropdown menu to choose "excellent/good/fair/poor", and then a description such as "This is a cool phone.".
Make sure that a user can give at most 3 reviews a day and cannot give a review to his own
items.
4. (6.25 pts) Implement a button called "Initialize Database." When a user clicks it, all
necessary tables will be created (or recreated) automatically. Each table will be populated with at
least 5 tuples so that each query below will return some results.

**Part 3: Deadline: Monday, 11/27, by midnight**
Based on parts 1 & 2, implement the following functionality using your selected programing language
and SQL with necessary GUI interfaces. Part 3 emphasizes both the interfaces and their integration
with backend database operations. Each item has 6.5 points.
1. List the most expensive items in each category.
2. List the users who posted at least two items that were posted on the same day, one has a category
of X, and another has a category of Y. In terms of the user interface, you will implement two
text fields so that you can input one category into each text field, and the search will return the
user (or users) who (the same user) posted two different items on the same day, such that one
item has a category in the first text field and the other has a category in the second text field.
3. List all the items posted by user X, such that all the comments are "Excellent" or "good" for
these items (in other words, these items must have comments, but these items don't have any
other kinds of comments, such as "bad" or "fair" comments). User X is arbitrary and will be
determined by the instructor.
4. List the users who posted the most number of items on a specific date like 5/1/2023; if there is
a tie, list all the users who have a tie. The specific date can be hard coded into your SQL select
query or given by the user.
5. List the other users who are favorited by both users X, and Y. Usernames X and Y will be
selected from dropdown menus by the instructor. In other words, the user (or users) C are the
favorite for both X and Y.
6. Display all the users who never posted any "excellent" items: an item is excellent if at least
three reviews are excellent.
7. Display all the users who never posted a "poor" review.
8. Display all the users who posted some reviews, but each of them is "poor".
9. Display those users such that each item they posted so far never received any "poor" reviews.
In other words, these users must have posted some items; however, these items have never
received any poor reviews or have not received any reviews at all.
10. List a user pair (A, B) such that they always gave each other "excellent" reviews for every single
item they posted.

Hint:
1) This is a team project. You are allowed to find and reused codes; however, make sure to
refer to the original source.
2) ONE submission per team is sufficient and all the team members will get the same grade.

How to submit:
1. The source code package. All files (source codes, class files, bat, and txt) should be
contained in a war or zip file called comp440_x_part1.zip for a team whose team number is
x submit via Canvas. (A team number will be assigned to your team by the deadline.)
2. A YouTube video. Use a recorder: https://www.apowersoft.com/free-online-screen-recorder.
And upload your video to www.youtube.com. I only need you to record your screen and
your voice for the project demo, not your face. You can add the YouTube URL to a readme
file inside your project directory or add it to the Canvas comment within your submission.
You can create slides for your presentation if that is helpful, Or you can use YouTube for
recording your video:
https://www.labnol.org/software/create-youtube-screencast/27936/
3. We may ask you to demo your project online via Zoom. It is only a demo between all your
team members and us (instructor and/or grader).

The project is to be done by at least two and a maximum of three students, but each student’s
contribution needs to be clearly stated in readme.txt. Start your project early, and ask questions if
you have doubts. Do not wait until the last minute. 
