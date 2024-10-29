from flask import render_template
from rogues_den import app, db


@app.route('/')
def home():
    return render_template('base.html')