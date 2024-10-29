from flask import render_template
from rogues_den import app, db
from rogues_den.models import User, Character


@app.route('/')
def home():
    return render_template('base.html')
