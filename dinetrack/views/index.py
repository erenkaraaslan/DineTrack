 
import os
import flask
import dinetrack
from flask import session
APP = flask.Flask(__name__)

@dinetrack.app.route('/')
def show_index():
	if 'username' not in session:
		flask.redirect(flask.url_for('account_login'))
	return flask.render_template("index.html")

def account_login():
	#Code for account login
	#Initialize session
	return flask.render_template("index.html")