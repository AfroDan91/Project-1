# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Employees, Departments



class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY = 'YOUR_SECRET_KEY',
            WTF_CSRF_ENEBLED=False
        )

        return app

    def setUp(self):
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

        db.session.add(dan)
        db.session.add(grant)
        db.session.add(amii)
        db.session.add(lucas)
        db.session.add(logan)

        db.session.commit()

    
    def tearDown(self):
        db.drop_all()


class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for("home"))
        assert "Daniel" in response.data.decode()


class TestCreate(TestBase):
    def test_add_emp(self):
        
        with self.client:
            response = self.client.post(
                url_for("add_emp"),
                data={"emp_fname": "bob", "emp_lname": "bob", "emp_email": "bob", "works_in" :'departments'},
                #data=dict(emp_fname = "bob", emp_lname = "bob",  emp_email = "bob", dep_name =(1, 'Sales')),
                follow_redirects=True

            )
            #self.assertEqual(response.status_code, 200)
            assert "bob" in response.data.decode()
        #self.assertIn(b'bob', response.data)


          
class testRead_dep(TestBase):
    def test_departments(self):
        response = self.client.get(url_for("dep"))
        assert "Sales" in response.data.decode()


class TestUpdate(TestBase):
    def test_update_emp(self):
        response = self.client.post(
            url_for("update_role", id=1),
            data=dict(departments=Departments(dep_name= 'Sales')),
            follow_redirects=True
            )
        assert "Sales" in response.data.decode()


class TestDel(TestBase):
    def test_delete(self):
        response = self.client.post(
            url_for("del_emp", id=1),
            follow_redirects=True
            )
        assert "Daniel" not in response.data.decode()
        self.assertEqual(response.status_code, 200)














# # Create the base class
# class TestBase(TestCase):
#     def create_app(self):

#         # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
#         app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
#                 SECRET_KEY='TEST_SECRET_KEY',
#                 DEBUG=True,
#                 WTF_CSRF_ENABLED=False
#                 )
#         return app

#     def setUp(self):
#         """
#         Will be called before every test
#         """
#         # Create table
#         db.create_all()

#         # Create test registree
#         sample1 = Register(name="MissWoman")

#         # save users to database
#         db.session.add(sample1)
#         db.session.commit()

#     def tearDown(self):
#         """
#         Will be called after every test
#         """

#         db.session.remove()
#         db.drop_all()

# # Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
# class TestViews(TestBase):

#     def test_home_get(self):
#         response = self.client.get(url_for('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'MissWoman', response.data)

# # Test adding 
# class TestAdd(TestBase):
#     def test_add_post(self):
#         response = self.client.post(
#             url_for('home'),
#             data = dict(name="MrMan"),
#             follow_redirects=True
#         )
#         self.assertIn(b'MrMan',response.data)