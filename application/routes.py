from flask import Flask, redirect, url_for, render_template, request
from sqlalchemy.orm import session
from . import app, db
from .models import Employees, Departments, Add_Employee, Select_Department
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



@app.route("/")
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = Add_Employee()
    emp_list = Employees.query.all() #brings the database of employees in 
    deps = Departments.query.all()

    return render_template('home.html', emps=emp_list, form=form)

@app.route('/create_employee', methods=['GET', 'POST'])
def add_emp():
    form = Add_Employee()
    if request.method == 'POST':
        deps = Departments.query.all()
        form.works_in.choices = [(dep.dep_id, dep.dep_name) for dep in deps]

        new_emp = Employees(
                        emp_fname=form.emp_fname.data, emp_lname=form.emp_lname.data,
                        emp_email=form.emp_email.data, department_id=form.works_in.data
                            )
        db.session.add(new_emp)
        db.session.commit()

        return redirect(url_for('home'))
    
    else:
        deps = Departments.query.all()
        form.works_in.choices = [(dep.dep_id, dep.dep_name) for dep in deps]

        return render_template('add.html', form=form)

    
@app.route('/employees')
def emp():
    pass

@app.route('/department')
def dep():
    deps = Departments.query.limit(5).all()
    list2 = []
    for dep in deps:
        list2.append([dep.dep_name])

    return render_template('deps.html', deps=list2)

@app.route('/about')
def about():
    pass

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_role(id):
    form = Add_Employee()
    e2u = Employees.query.get(id)
    deps = Departments.query.all()
    form.works_in.choices = [(dep.dep_id, dep.dep_name) for dep in deps]
    if request.method == 'POST':
        e2u.department_id= form.works_in.data
        db.session.commit()
        return redirect(url_for('home'))
                            

    else:
        return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def del_emp(id):
    e2r = Employees.query.get(id)
    db.session.delete(e2r)
    db.session.commit()
    return redirect(url_for('home'))



# @app.route('/')
# @app.route('/home', methods=['GET', 'POST'])
# def showt():
#     list1 = Task.query.filter_by(completed=False)
#     list2 = []
#     list3 = []
#     for task in list1:
#         list2.append(task.name)
#         list3.append(task.description)
#     return render_template('home.html', name=list2, desc=list3)

# @app.route('/add', methods=['GET', 'POST'])
# def add_task():
#     form1 = AddTaskForm()
#     if request.method == 'POST':
#         task_name = form1.task_name.data
#         taskdesc = form1.task_desc.data

#         if len(task_name) != 0:
#             newt = Task(name=str(task_name), description=str(taskdesc))
#             db.session.add(newt)
#             db.session.commit()
#             return redirect(url_for('showt'))  

#     return render_template('add.html', form1=form1)

# @app.route('/completed')
# def showc():
#     list1 = Task.query.filter_by(completed=True) 
#     list2 = []
#     for task in list1:
#         list2.append(task.name)

#     return render_template('completed.html', tasks=list2,)

# @app.route('/updateDesc', methods=['GET', 'POST'])
# def udesc():
#     form = AddTaskForm()
    
#     if request.method == 'POST':
#         task_name = form.task_name.data
#         taskdesc = form.task_desc.data
    
#         t2u = Task.query.filter_by(name=task_name).first()
        
#         t2u.description = taskdesc
#         db.session.commit()
#         return redirect(url_for('showt'))  

#     return render_template('updateDesc.html', form=form) #task=task_name, desc=taskdesc)

# @app.route('/delete', methods=['GET', 'POST'])
# def td():
#     form = AddTaskForm()
    
#     if request.method == 'POST':
#         task_name = form.task_name.data
#         taskdesc = form.task_desc.data
    
#         t2d = Task.query.filter_by(name=task_name).first()
        
#         db.session.delete(t2d)
#         db.session.commit()
#         return redirect(url_for('showt'))  

        #return render_template('delete.html', form=form) #task=task_name, desc=taskdesc)