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

### **Design Outline** 
For my application I have decided to go with a file restriction tool. To begin creating this I will need to design multiple databases to house my users, access levels and accessible files.
To display these I have created an entity relationship diagram displaying the 3 main components of my app.

![ERD1](https://i.imgur.com/zqFzORE.png)

As you can see from the picture, mapping it out made apparent an issue with my relational databases. 
Due to using MySQL to build my data bases and they don't support many-to-many relations I will needed to amend my diagram and input an additional step to split the relation from Users to Files.

The resolution to my issue came in the form of a new database called Authenticator which stands as buffer between the Users and Files databases. 

![ERD2](https://i.imgur.com/hx79vUr.png)

This resolves the many-to-many issue by combining the files into groups allowing for multiple users to access 1 group but the group contains multiple files. 


The EDR design I settled on looks like this;

![ERD4](https://i.imgur.com/7IW14a7.png)

As you can see its a lot different from how it was originally, these diagrams are very important for mapping out databases before building them to avoid running into these problems when there are potentially thousands of entries that my need amending.  