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

![ERD2](https://i.imgur.com/510ur8K.png)

As you can see its a lot different from how it was originally, these diagrams are very important for mapping out databases before building them to avoid running into these problems when there are potentially thousands of entries that my need amending. 







![Riskass](https://i.imgur.com/M6H7xsA.png)




|     | Date Added |                  Description                  |                                               Evaluation                                              | Likelihood | Impact Level |             Responsibility            |                                                     Response                                                     |                                                               Control Measures                                                               |
|:---:|:----------:|:---------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|:----------:|:------------:|:-------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|
|  1. | 30/06/2021 |                  VM goes down                 |                                            App goes offline                                           |     Low    |     High     |                  GCP                  |                                    Recreate infrastructure on another machine                                    |                                             Use repo to recreate version on another working vm.                                              |
|  2. | 30/06/2021 |      Wrong version merged to live version     |                                    Possible loss of functionality                                     |   Medium   |     High     |               Developer               |                                      Revert back to previous stable  version                                     |              Conduct rigorous testing before anything is pushed to production environment. Restrict access to that environment.              |
|  3. | 08/07/2021 |                 GCP goes down                 |                                         Application goes down                                         |  Very Low  |     High     |                  GCP                  |                                 Recreate on another cloud host like AWS or Azure                                 |            Research hosts before using their services. Have VCS to allow deployment with another host should current one go down.            |
|  4. | 12/07/2021 |               Run over deadline               |                                    Product isn't ready for review                                     |     Low    |     High     |               Developer               |                     Produce as much as possible and display most up to date version possible                     |            Manage project with Jira to keep on track with deadline. Employ other developers to help if things start to fall behind           |
|  5. | 12/07/2021 |            Error in database setup            |                                  Product doesn't perform as it should                                 |     Low    |     High     |               Developer               | Conduct tests to ensure data is formatted and input correctly. roll back to previous working version if possible |                                      Validate data and automate the input of data as much as possible.                                       |
|  6. | 12/07/2021 |     Loss of password to developer systems     |                          Unable to conduct maintenance or updates to product                          |  Very Low  |    Medium    |               Developer               |                                 Use recovery methods to gain access to account.                                  |                                            Keep passwords stored securely in a password manager.                                             |
|  7. | 12/07/2021 |        Ransome ware attack on computers       |             developers are locked out of their computers and application is taken offline             |     Low    |     High     | Anyone in contact with backend access |              Remove computers form the compromised network or use new ones to connect to remote vm.              |                              Keep backups of systems and data where possible. Use offsite data storage and vms.                              |
|  8. | 12/07/2021 | Developer sells customers private information |                company is brought under scrutiny and potential drop in public opinion                 |  Very Low  |     High     |         Hiring staff/ managers        |                       Try to find out who gave the leak and who too. Work with authorities                       | Vet staff and have them sign disclosures. Only allow access to personal information to people who are cleared and have a reason to need it.  |
|  9. | 12/07/2021 |             Company goes bankrupt             |                                          Application is sold                                          |  Very Low  |   Very High  |        CEO/ Financial director        |                              Create copies of application for use in other projects.                             |     provide accurate figures of traffic and sales via automated capture methods to ensure business decisions are made with all the facts.    |
| 10. | 12/07/2021 | Product licence runs out and is not renewed.  | Development can be stopped or severely hampered. Company fined per machine using unlicensed software  |     Low    |    Medium    |            Licence holders            |                                  Find the licence hold and have licence renewed                                  |                                 Keep licence expiry dates tracked and automatically renewed where possible.                                  |