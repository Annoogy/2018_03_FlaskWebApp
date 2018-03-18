import pandas as pd
from flask import Flask, render_template
#from flask_bootstrap import Bootstrap


app = Flask(__name__)
#Bootstrap (app)


@app.route('/')
def cover():
    return render_template('cover.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
s