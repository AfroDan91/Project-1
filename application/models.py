from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class Employees(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_fname = db.Column(db.String(25),nullable=False)
    emp_lname = db.Column(db.String(25),nullable=False)
    emp_email = db.Column(db.String(50),nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.dep_id'), nullable=False)

class Departments(db.Model):
    dep_id = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(20),nullable=False)
    worker = db.relationship('Employees', backref='departments')

class Add_Employee(FlaskForm):
    emp_fname =  StringField('Employee First Name')
    emp_lname =  StringField('Employee Last Name')
    emp_email =  StringField('Employee Email Address')
    submit = SubmitField('Add Employee')

    
class Select_Department(FlaskForm):
    department = SelectField('Pick a department', choices=[])
    submit = SubmitField('Add Task')