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
But the two main things is that they keep the code working. It is very easy when not running tests like these to make a change that has ripple effects out of the expected working area. As the scope of unit tests can span the width of your entire project its very easy to detect these with 1 line of code in the terminal.

And the user is getting the desired outcomes of their actions when interacting with the app. Working code is one of the corner stones of the Agile methodology and testing helps ensure I meet that criteria. 

To conduct my unit testing I used Pytest and pytest-cov, both were installed using the pip3 installation method. 
The results of the tests were:

![Pytest1](https://i.imgur.com/P6omcMa.png)

These tests confirm that information was able to be added, read and removed from the database and that the HTML displayed that information as expected.
The coverage results also show that all major aspects of the code have been tested. It is important to test as much as possible to catch as much as possible before the code reaches the live environment. 

Further more I utilised Jenkins to further automate my testing. This enabled me to get a copy of my tests each time I made a push to git hub as well as being able to run them myself. This helps mitigate the chances of broken code reaching the live environment and causing issues for the end user. 

Jenkins works by receiving webhooks from github when a new push is made. The webhooks tell Jenkins what branch has been updated and when. Jenkins then clones down the repository and runs a predetermined set of instructions. 

My Jenkins build looks like this:

![jenk](https://i.imgur.com/kIfedjE.png)

**Step 1**
The initial step is creating a bash script that the Linux machine running Jenkins can interpret.

**Step 2**
Next is to install; python3 - the language the rest of the code works on, python3 -pip - the package management system that allows us to install the modules needed, and python3-venv - the package that allows virtual environments to be set up. 
The python3-venv is especially important as we can have Jenkins test multiple repos which might have different dependences. This allows us to keep those dependences separated easily to avoid clashing or unintended bugs.

**Step 3**
Now it initiate the virtual environment creating a safe/ clean space to install our required modules. 

**Step 4**
Now as I have saved the requirements in a text file I don't need to write them out each time I can just call them from the .txt file.
<details>
  <summary>requirements.txt</summary>

![req](https://i.imgur.com/B3feoMC.png)
</details>
<br />

**Step 5**
Lastly is to run the tests just as I would in my own bash terminal. 
<details>
  <summary>The full output of a build can be seen here</summary>

```
Started by user admin
Running as SYSTEM
Building in workspace /home/jenkins/.jenkins/workspace/Project-1
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /home/jenkins/.jenkins/workspace/Project-1/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/AfroDan91/Project-1.git # timeout=10
Fetching upstream changes from https://github.com/AfroDan91/Project-1.git
 > git --version # timeout=10
 > git --version # 'git version 2.17.1'
 > git fetch --tags --progress -- https://github.com/AfroDan91/Project-1.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/Feature-app^{commit} # timeout=10
Checking out Revision 1323c08f052219f67d20d553f762af0d9debf1c3 (refs/remotes/origin/Feature-app)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 1323c08f052219f67d20d553f762af0d9debf1c3 # timeout=10
Commit message: "all tests working!"
First time build. Skipping changelog.
[Project-1] $ /bin/bash /tmp/jenkins5030874721363002920.sh
Reading package lists...
Building dependency tree...
Reading state information...
python3 is already the newest version (3.6.7-1~18.04).
python3-pip is already the newest version (9.0.1-2.3~ubuntu1.18.04.5).
python3-venv is already the newest version (3.6.7-1~18.04).
The following package was automatically installed and is no longer required:
  libnuma1
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.
Requirement already satisfied: attrs==21.2.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 1))
Requirement already satisfied: click==8.0.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 2))
Requirement already satisfied: coverage==5.5 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 3))
Requirement already satisfied: dataclasses==0.8 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 4))
Requirement already satisfied: Flask==2.0.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 5))
Requirement already satisfied: Flask-SQLAlchemy==2.5.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 6))
Requirement already satisfied: Flask-Testing==0.8.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 7))
Requirement already satisfied: Flask-WTF==0.15.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 8))
Requirement already satisfied: greenlet==1.1.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 9))
Requirement already satisfied: importlib-metadata==4.6.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 10))
Requirement already satisfied: iniconfig==1.1.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 11))
Requirement already satisfied: itsdangerous==2.0.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 12))
Requirement already satisfied: Jinja2==3.0.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 13))
Requirement already satisfied: MarkupSafe==2.0.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 14))
Requirement already satisfied: packaging==21.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 15))
Requirement already satisfied: pkg-resources==0.0.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 16))
Requirement already satisfied: pluggy==0.13.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 17))
Requirement already satisfied: py==1.10.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 18))
Requirement already satisfied: PyMySQL==1.0.2 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 19))
Requirement already satisfied: pyparsing==2.4.7 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 20))
Requirement already satisfied: pytest==6.2.4 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 21))
Requirement already satisfied: pytest-cov==2.12.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 22))
Requirement already satisfied: SQLAlchemy==1.4.20 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 23))
Requirement already satisfied: toml==0.10.2 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 24))
Requirement already satisfied: typing-extensions==3.10.0.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 25))
Requirement already satisfied: Werkzeug==2.0.1 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 26))
Requirement already satisfied: WTForms==2.3.3 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 27))
Requirement already satisfied: zipp==3.5.0 in ./venv/lib/python3.6/site-packages (from -r requirements.txt (line 28))
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/jenkins/.jenkins/workspace/Project-1
plugins: cov-2.12.1
collected 5 items

application/tests/test_unit.py .....                                     [100%]

=============================== warnings summary ===============================
venv/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:873
  /home/jenkins/.jenkins/workspace/Project-1/venv/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:873: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
    'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '

-- Docs: https://docs.pytest.org/en/stable/warnings.html

----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                             Stmts   Miss  Cover
----------------------------------------------------
application/__init__.py              9      0   100%
application/models.py               25      0   100%
application/routes.py               41      0   100%
application/tests/__init__.py        0      0   100%
application/tests/test_unit.py      57      0   100%
----------------------------------------------------
TOTAL                              132      0   100%

========================= 5 passed, 1 warning in 0.96s =========================
Finished: SUCCESS
```
</details>
<br />
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

This is where most of the functionality lives. 
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


## **Acknowledgements**

### Trainers
Oliver Nichols
Ryan Wright
Victoria Scare

### colleagues
Eral Gray

### Tools
The internet
<br />
<br />
<br />

## **License**

<details>

  <summary>View General Public License</summary>
                      GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.


</details>