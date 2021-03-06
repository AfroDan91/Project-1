from application import db
from application.models import Employees, Departments, Add_Employee, Select_Department

db.drop_all()
db.create_all()
sales = Departments(dep_name = 'Sales')
hr = Departments(dep_name = 'Human Resources')
ceo = Departments(dep_name = 'CEO')
cs = Departments(dep_name = 'Customer Service')
jani = Departments(dep_name = 'Janitor')
letgo = Departments(dep_name = 'No Longer Works Here')

db.session.add(sales)
db.session.add(hr)
db.session.add(ceo)
db.session.add(cs)
db.session.add(jani)
db.session.add(letgo)

dan = Employees(emp_fname = 'Daniel', emp_lname = 'Wordie', emp_email = 'daniel@aol.com', departments = Departments(dep_name='Janitor'))
grant = Employees(emp_fname = 'Grant', emp_lname = 'Cornish', emp_email = 'k08@ntlworld.com', departments = Departments(dep_name='Janitor'))
amii = Employees(emp_fname = 'Amii', emp_lname = 'Wordie', emp_email = 'amii@argos.com', departments = Departments(dep_name='Customer Service'))
lucas = Employees(emp_fname = 'Lucas', emp_lname = 'Wordie', emp_email = 'lucasaurus1@crazyboy.com', departments = Departments(dep_name='CEO'))
logan = Employees(emp_fname = 'Logan', emp_lname = 'Wordie', emp_email = 'logie3453@aol.com', departments = Departments(dep_name='Sales'))
stacey = Employees(emp_fname = 'Stacey', emp_lname = 'Cornish', emp_email = 'xlx_stacey_xlx@ntl.com', departments = Departments(dep_name='Sales'))
liam = Employees(emp_fname = 'Liam', emp_lname = 'Cornish', emp_email = 'the_big_lc@hotmail.com', departments = Departments(dep_name='Human Resources'))
fin = Employees(emp_fname = 'Findley', emp_lname = 'Cornish', emp_email = 'grumpykid@aol.com', departments = Departments(dep_name='Sales'))
paul = Employees(emp_fname = 'Paul', emp_lname = 'Lagah', emp_email = 'pol1 @emp_email.com', departments = Departments(dep_name='Janitor'))
jack = Employees(emp_fname = 'Jack', emp_lname = 'McAlorum', emp_email = 'ILOVEROCKS@someuni.com', departments = Departments(dep_name='CEO'))
ewen = Employees(emp_fname = 'Ewen', emp_lname = 'MacVicar', emp_email = 'Itz_Pr0H43D5H07@aol.com', departments = Departments(dep_name='Janitor'))
steven = Employees(emp_fname = 'Steven', emp_lname = 'Gray', emp_email = 'lulz@meme.com', departments = Departments(dep_name='No Longer Works Here'))
calum = Employees(emp_fname = 'Calum', emp_lname = 'idonthavealastname', emp_email = 'anon@secret.com', departments = Departments(dep_name='CEO'))
# = Employees(emp_fname = '', emp_lname = '', emp_email = '', department = '')

db.session.add(dan)
db.session.add(grant)
db.session.add(amii)
db.session.add(lucas)
db.session.add(logan)
db.session.add(stacey)
db.session.add(liam)
db.session.add(fin)
db.session.add(paul)
db.session.add(jack)
db.session.add(ewen)
db.session.add(steven)
db.session.add(calum)

db.session.commit()