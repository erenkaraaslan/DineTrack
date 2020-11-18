 
import os
import flask
import dinetrack
from flask import session
from flask import request
APP = flask.Flask(__name__)

@dinetrack.app.route('/', methods=['POST', 'GET'])
def show_index():
	if 'username' not in session:
		flask.redirect(flask.url_for('account_create'))
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		#Verify user against DB
	return flask.render_template("index.html")

@dinetrack.app.route('/accounts/create/', methods=['POST', 'GET'])
def account_create():
	#Code for account login
	#Initialize session
	return flask.render_template("create.html")