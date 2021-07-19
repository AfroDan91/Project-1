from flask import Flask, redirect, url_for, render_template, request
from application import app, db
from application.models import Employees, Departments, Add_Employee, Select_Department
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    emp_list = Employees.query.all()
    list2 = []
    for emp in emp_list:
        list2.append([emp.emp_fname, emp.emp_lname, emp.emp, emp.dep_name])
    return render_template('home.html', emps=list2)

    pass

@app.route('/employees')
def emp():
    pass

app.route('/department')
def dep():
    pass

app.route('/about')
def about():
    pass

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')



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

#     return render_template('delete.html', form=form) #task=task_name, desc=taskdesc)