from application import db

class Employees(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_fname = db.Column(db.String(25),nullable=False)
    emp_lname = db.Column(db.String(25),nullable=False)
    emp_email = db.Column(db.String(50),nullable=False)

class Depertments(db.Model):
    dep_id = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(20),nullable=False)