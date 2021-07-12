from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main_page():
    pass

@app.route('/home')
def home():
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