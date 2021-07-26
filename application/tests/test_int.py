# Import the necessary modules
from flask import url_for
from flask_testing import LiveServerTestCase
from flask_testing.utils import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen

# import the app's classes and objects
from application import app, db
from application.models import Employees, Departments



class TestBase(LiveServerTestCase):

    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY = 'YOUR_SECRET_KEY',
            LIVESERVER_PORT=self.TEST_PORT
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

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless') # must be headless

        self.driver = webdriver.Chrome(options=chrome_options) 

        db.create_all() # create schema before we try to get the page
        self.driver.get(f'http://localhost:{self.TEST_PORT}/')

    
    def tearDown(self):
        db.drop_all()
        self.driver.quit()


    def test_server_is_up_and_running(self):
        response = urlopen(f"http://localhost:{self.TEST_PORT}")
        assert response.code == 200

class Testadd(TestBase):
    def test_add(self):
        #move from home to add page
        self.driver.find_element_by_xpath("/html/body/h3/a[2]").click() 

        #fills in form
        self.driver.find_element_by_xpath('//*[@id="emp_fname"]').send_keys("Test")
        self.driver.find_element_by_xpath('//*[@id="emp_lname"]').send_keys("Test")
        self.driver.find_element_by_xpath('//*[@id="emp_email"]').send_keys("Test")

        #submits form
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        result = self.driver.find_element_by_xpath("/html/body/div[6]")
        assert "Test" in result.text


class Testup(TestBase):
    def test_up(self):
        #move from home to update
        self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()

        #select role
        self.driver.find_element_by_xpath('//*[@id="works_in"]').click()
        self.driver.find_element_by_xpath('//*[@id="works_in"]/option[1]').click()

        #submit
        self.driver.find_element_by_xpath('//*[@id="submit2"]').click()

        result = self.driver.find_element_by_xpath("/html/body/div[1]")
        assert "Sales" in result.text


class Testdel(TestBase):
    def test_delp(self):
        #move from home to delete
        self.driver.find_element_by_xpath("/html/body/div[1]/a[1]").click()

        result = self.driver.find_element_by_xpath("/html/body/div[1]")
        assert "Daniel" not in result.text