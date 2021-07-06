# **Project-1 - CRUD Application**

### **Introduction**
The overall objective of this project is to design an application which has  create, read, update and delete (CRUD) functionality using the Agile methodology we have learned. 
The main skills and fundamentals this will display are:
* project management ability
* effective use of the python coding language
* the effective use of version control systems like Git
* the use of the Agile principles
* the use of the continuous design/integration models
* the effective use of databases
By displaying these core aspects of my learning I hope to show I have a working knowledge and clear understanding of the aspects and am able to effectively apply them when necessary. 


### **Design Ideas**
I began the process of  coming up with ideas as a brainstorm which produced 4 viable results.

The first Idea was a hero insights application, this would have allowed a user to input results from games played in Dota2 to gain a deeper understanding of how the hero's they played effected the likelihood of a win. 
I initially liked this idea as it relates to a game I am very passionate about however, I ultimately rejected it as the one I settled on was more relevant to my work aspirations.

The third idea was a customer purchasing log with customer ids and transactions history, allowing insights into purchase behavior. And the fourth was a country vs currency and the exchange rate between them however I rejected both as I thought more about the second and came to the conclusion that it was the most relevant and easiest to map out in my mind. 

The second Idea was a user database with authentication levels allowing the administrator to lock certain files behind different access levels. I felt this to be the most relevant Idea to my work aspirations and I felt most confident with the theory of it. 

Having worked on the user database and mapping it out in an ERD I came to the conclusion that the idea in its current form would require 3-4 databases all of which would need their own CRUD functionality to act in the way I envisaged. This lead me to simplifying it down to its 2 main components, users and roles. The application would now focus on delivering a a series of roles and a database with users who can be assigned to a given role. This would account for the desired CRUD functionality while being much more realistically achievable.
On the bright side the factors that were dropped for now will provide excellent stretch goals should it achieve its man functionality with time to spare. 

### **Design Outline** 
In the beginning  I decided to go with a file restriction tool. To begin creating this I will need to design multiple databases to house my users, access levels and accessible files.
To visualise these I created an entity relationship diagram displaying the 4 components that make up my app

![ERD4](https://i.imgur.com/7IW14a7.png)

It was at this point the scale of the idea became apparent and its viability called into question. 
I used the ERD to distil my idea down to its main components and mapped them out in a new ERD. This idea cuts out the majority of the chaff while still maintaining the the essence of the concept and core CRUD functionality.
The EDR design I settled on looks like this;

![ERD2](https://i.imgur.com/510ur8K.png[/img)

As you can see its a lot different from how it was originally, these diagrams are very important for mapping out databases before building them to avoid running into these problems when there are potentially thousands of entries that my need amending. 