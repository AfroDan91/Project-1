# **Project-1 - CRUD Application**

## **Introduction**
The overall objective of this project is to design an application which has  create, read, update and delete (CRUD) functionality using the Agile methodology we have learned. 
The main skills and fundamentals this will display are:
* project management ability
* effective use of the python coding language
* the effective use of version control systems like Git
* the use of the Agile principles
* the use of the continuous design/integration models
* the effective use of databases
By displaying these core aspects of my learning I hope to show I have a working knowledge and clear understanding of the aspects and am able to effectively apply them when necessary. 

<br />

## **Design Ideas**
I began the process of  coming up with ideas as a brainstorm which produced 4 viable results.

The first Idea was a hero insights application, this would have allowed a user to input results from games played in Dota2 to gain a deeper understanding of how the hero's they played effected the likelihood of a win. 
I initially liked this idea as it relates to a game I am very passionate about however, I ultimately rejected it as the one I settled on was more relevant to my work aspirations.

The third idea was a customer purchasing log with customer ids and transactions history, allowing insights into purchase behavior. And the fourth was a country vs currency and the exchange rate between them however I rejected both as I thought more about the second and came to the conclusion that it was the most relevant and easiest to map out in my mind. 

The second Idea was a user database with authentication levels allowing the administrator to lock certain files behind different access levels. I felt this to be the most relevant Idea to my work aspirations and I felt most confident with the theory of it. 

Having worked on the user database and mapping it out in an ERD I came to the conclusion that the idea in its current form would require 3-4 databases all of which would need their own CRUD functionality to act in the way I envisaged. This lead me to simplifying it down to its 2 main components, users and roles. The application would now focus on delivering a a series of roles and a database with users who can be assigned to a given role. This would account for the desired CRUD functionality while being much more realistically achievable.
On the bright side the factors that were dropped for now will provide excellent stretch goals should it achieve its man functionality with time to spare. 
<br />
<br />

## **Design Outline** 
In the beginning  I decided to go with a file restriction tool. To begin creating this I will need to design multiple databases to house my users, access levels and accessible files.
To visualise these I created an entity relationship diagram displaying the 4 components that make up my app

![ERD4](https://i.imgur.com/7IW14a7.png)

It was at this point the scale of the idea became apparent and its viability called into question. 
I used the ERD to distil my idea down to its main components and mapped them out in a new ERD. This idea cuts out the majority of the chaff while still maintaining the the essence of the concept and core CRUD functionality.
The EDR design I settled on looks like this;

![ERD2](https://i.imgur.com/7VHvHw7.png)

As you can see its a lot different from how it was originally, these diagrams are very important for mapping out databases before building them to avoid running into these problems when there are potentially thousands of entries that my need amending. 

I have included all the different forms my ERD took, in order of creation, below:
<details>
 <summary>Click to expand!</summary>
  
![ERD3](https://i.imgur.com/zqFzORE.png)

![ERD4](https://i.imgur.com/hx79vUr.png)

![ERD5](https://i.imgur.com/EiOhQo5.png)

![ERD6](https://i.imgur.com/7IW14a7.png)

![ERD7](https://i.imgur.com/510ur8K.png)

![ERD8](https://i.imgur.com/7VHvHw7.png)

</details>
<br />
<br />


## **Risk Assessments**

It is extremely important to conduct risk assessments on as many aspects of the applications design, deployment and continued development to help both avoid them in the first place and fix them asap.
Risk assessments can also allow you to pro-actively resolve issues before they impair or impede the app's design, development or deployment.  
Below is a table of identified risks, likelihood of occurring, impact level, restoration steps and avoidance steps.

![Riskass](https://i.imgur.com/M6H7xsA.png)

<br />
<br />

## **Project Tracking**

The last thing I needed to do before I could get into the physical design of the application was to utilise a project tracking tool. Using a tracking tool will help me keep on track of my ultimate goal and allow me to break down my project into smaller more manageable tasks. By doing this, I can map out a timeline to help me keep on tack with my work and ensure I don't slip behind. 

The project tracking tool I used was Jira. This was chosen primarily due to it being the main one I am familiar with. Using Jira I broke my work down to a series of epics and from their further down into user stories. 
The use of user stories really helps to imagen the app working and help envisage functionality and features to implement. 
Jira is also a good choice due to its design being catered to an Agile methodology. Having built in sprint tracking made it easy to conduct my work while sticking to the Agile principles .

My Jira board looked like this in the beginning

![Jira](https://i.imgur.com/EcSxTb1.png)

With epics arranged by database functionality set out in the EDR.

As the project matured so did the content and design of by Jira board. Towards the end of the development process the Jira board looked like this:

![Jira2](https://i.imgur.com/zT5XCN3.png)

I added user stories throughout the development process as each parts design brought up new features and functionality that could be added that I never thought of during the initial brainstorming. 

<br />
<br />

## **Test Driven Development**


The next step in the development process is the use of unit testing. Both the Agile and DevOps principles teach the benefits of this in the way they operate. 
Some of the key benefits of carrying out unit tests are:
- They decrease the Time to Discovery (TTD)
- They allow for a wide range of tests to be completed at once.
- They only need to be written once
But the main thing is that they keep the code working. It is very easy when not running tests like these to make a change that has ripple effects out of the expected working area. As the scope of unit tests can span the width of your entire project its very easy to detect these with 1 line of code in the terminal.

To conduct my unit testing I used Pytest and pytest-cov, both were installed using the pip3 installation method. 
The results of the tests were:

![Pytest1](https://i.imgur.com/P6omcMa.png)

These tests confirm that information was able to be added, read and removed from the database and that the HTML displayed that information as expected. 
If I have another sprint on this project one of my main priorities would be adding additional test cases to improve the detection of issues involving edge cases.

<br />
<br />

## **Programs, Applications and Installs**

During the development of my project and its dependencies I have used a verity of different tools some of which I have already spoken about. 

<details>
  <summary>Here is a breakdown of the majority of the tools I utilized</summary>
  
This is my pipeline. 

![Pipeline](https://i.imgur.com/2TQASoi.png)

It shows what tools I used and where I used them form the major elements of the projects. Below that is a more detailed breakdown of the elements, why they were used and the likelihood of using them again based on my experience with them throughout this project. 


<details>
  <summary>Source Code</summary>

## Python
I chose python as my source code to fulfill the requirements of the project as it is the language I have the most knowledge of and ability in.  It was also a good choice doe to its extensive use in the industry and as a result has many guide, information sites and knowledge bases to help during the development process. 
In choosing python I was also able to utilize some of its modules both built in and external
Some of the modules I used were:
- Flask - This is a python driven micro framework which enables easy design and construction of web applications.
- SQLAlchemy - This is an extension for Flask, allowing it to manipulate data in relational databases with pythonic code.
- wtforms - This is an extension for Flask, allowing easy capture of data from a user in the shape of a form
- Pytest - This allows for unit testing to occur enabling the length and breadth of a project to be tested with 1 line of code. 

In reflection if I was to do another project like this I would use python again as it was easy to use and find further information on. 

## Visual Studio Code
VS Code is a source-code editor which offers features including debugging, syntax highlighting, intelligent code completing and embedded git. This made it the obvious choice for me along with being something I have used in the past. 
10/10 will use again.

</details>

<details>
  <summary>Version Control</summary>

## GitHub
Git hub was my version control service of choice as I have had some experience in it previously and it is very widely used. 
I really enjoyed using Git Hub as it was very easy to use and worked well with other tools I used such as Jenkins. 
If I were to work on another project like this I would definitely consider using GitHub again.
</details>

<details>

  <summary>Project Tracking</summary>

## Jira
I have already given the reasons why I used Jira over other project tracking tools and should I will likely use it again on future projects. 

</details>

<details>

  <summary>CI Server / Unit Testing</summary>
  
## Jenkins
I chose Jenkins to use for both my unit testing and CI server because it is the service I have the most experience with. I made use of its web hook capabilities to automatically run my unit tests through it Which made life a lot easier when it came to the testing phase.

I will very likely be using this again on future projects due to its ease of use. 

</details>

<details>

  <summary>Miscellaneous </summary>
  
## Google Could Platform
GCP was my cloud provider for my project due to its free trial period I made good use of the many free services it offers and will likely use it again in the future as a result of its easy to use website and easy to understand services. 

## MySQL
I chose MySQL for its entry level understandability. The interactions with python via SQLAlchemy made it easy to manipulate the database as needed. 
In a future project I may use this again however it doesn't handle many to many relationships resulting in workarounds needing to be utilised should a many to many relationship occur.

## Linux
Last but not least I used Linux, Ubuntu 18 for my virtual machine as it is open source meaning there is a tonne of help websites and a large community behind it when you get stuck. Another big reason was its customisability. There are a mountain of addons, plug-ins and apps to expand its functionality and tailor it to your needs. This came in handy during the project. 
A final thing is it's very light weight making it very good for using on virtual machines as it doesn't cost to much to have it running. 

I will definitely be using Linux in future projects. 

</details>


</details>

<br />
<br />

## **Tour of the app**

<details>
 <summary>Here is a pictorial tour of my application and a demonstration of it in use.  </summary>

## Home Page
![homepage](https://i.imgur.com/CfcAYxi.png)
this is where most of the functionality lives. 
At the top (1) is a list of links to the other pages that are used. This is present across all of the usable pages and was created by using the {% extends %} html feature. This allows me to write the html links once and pull them onto any page that should have them.  
Below that (2) there is a list of all users in the database. Their first name, last name and current position are all displayed clearly to the viewer using get requests from the data base. 
Under their names there are two options to choose;
Delete removes the entry from the database by adding the emp_id (which is the primary key on the Employees database) to the dynamic url for the delete page. 
The delete page then uses that to delete the entry from the database and automatically redirects the user back to the home screen when completed. 

Update role allows you to change the role registered to them after the '|'


## Update Role Page
![updatepage](https://i.imgur.com/fduKCPY.png)
Having clicked the 'Update Role' option on the homepage we are brought to this one. 
here (1) you can select a new role from the select form menu which is populated from the database it's self. 
and (2) is a submit field to activate the post request to the database. 
After this is pressed  the change is committed and your are automatically redirected back to the homepage. 


## Add employee Page
![addemp](https://i.imgur.com/ssGNcR4.png)
When arriving on the Add Employee page you are met with 3 string fields(1) prompting you for the first and last name and the email of the new entrant. Under that you are asked to choose a department(2) to add the new entry too just like on the update page.
Finally under that again, you are able to create a post request by hitting the "add Employee" button (3) which will commit the above 4 fields into the database and redirect the user back to the homepage where they can see their new entry at the bottom. 


## View Departments Page
![viewdep](https://i.imgur.com/er00mWQ.png)
This page allows the user to view all the existing departments. In a future iteration of the app I hope to fill this page out more and format it more appropriately. 




</details>

<br />
<br />

## **Sprit Retrospective**

Following my first spring on the project here is a break down of the key points that went well, went poorly and ambitions for a future sprint.

### **What went well?**

The project as a whole went very well I utilised many of the skills I learned in the previous weeks and for parts I didn't know I used information accessed from the internet, tutorial videos from the trainers, colleges and the QA Community resources.
One big success was creating the CRUD functionality on day 1 I was very please with my self. The to-do app provided an excellent spring board to start from having completed very similar steps to the ones I need to take in this project on that previous one. 
Another element that went well was the Jenkins integration which worked first time. The only hiccup I had with that was forgetting to update the webhook IP address after restarting the server on day 3 as the dynamic IP had changed. 


### **What I could have done better?**
The unit testing was the part that gave me the most grief. It was the part I had the least confidence in from the training and I struggled to get the coverage and tests to complete fully. 
The biggest hurdle I faced with unit testing was my homepage which pytest couldn't read. Unfortunately I didn't realise that was where the problem was coming from until some hours later when a teammate pointed it out. 
However when the issue was identified it was rectified very shortly after. 

For future projects I will implement a wider array of tests which should help narrow down the exact location of issues much quicker, reducing Time To Discovery (TTD).

I will also validate the information in my database better as there were a few duplicate entries generated upon creation. As I didn't implement CRUD functionality for the Departments data base I was unable to easily remove them.

Another thing I will do better next time is add comments to my code as I go. This will greatly increase the readability of my code and help speed up development as I wont need to analyse it each time I come back to code written previously. 

### **Improvements**

I have a couple of ambitions for this project should I get another opportunity to arrange a sprint for it:
- Log in capability
- Time out of login
- User accounts
- A way of transmitting access granted by department to a user's account. 
- About page
- CRUD for departments
- Filtering options on home and departments page
- Polish the aesthetics of the front end

Some of these were out of scope for the original project and the others were of a lower priority due to the requirements of the project. 
With these steps completed and a few more not mentioned this could become a marketable product. 