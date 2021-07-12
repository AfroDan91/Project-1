from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def wellcome_message():
    return redirect(url_for('home_page'))

@app.route('/home')
def home_page():
    return "Hello and welcome to my app"

        


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')