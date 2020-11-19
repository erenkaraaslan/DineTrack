 
import os
import flask
import dinetrack
from dinetrack.database import get_db, close_connection
from flask import session
from flask import request
APP = flask.Flask(__name__)

@dinetrack.app.route('/', methods=['POST', 'GET'])
def show_index():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		db = get_db()
		cur = db.cursor()
		query = "SELECT password FROM users WHERE username = '{}';".format(username)
		cur = cur.execute(query);
		db_password = cur.fetchall()[0][0]
		if password == db_password:
			session['username'] = username
			print('User logged in!')
			#Load some other page to show
		#Verify user against DB
	return flask.render_template("index.html")

@dinetrack.app.route('/accounts/create/', methods=['POST', 'GET'])
def account_create():
	#Code for account create
	#Input to db with query
	#Get the db
	if request.method == 'POST':
		inputs = request.form
		db = get_db()
		cur = db.cursor()
		query = "INSERT INTO users(username, firstname, lastname, email, proffilename, password) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(inputs['username'], inputs['firstname'], inputs['lastname'], inputs['email'], inputs['prof_pic'], inputs['password'])
		cur.execute(query)
		db.commit()
		#Set the flask session details
		session['username'] = inputs['username']
		return flask.redirect(flask.url_for("show_index"))
	return flask.render_template("create.html")

#Call this url for any logout link
@dinetrack.app.route('/accounts/logout', methods=['POST', 'GET'])
def logout():
	#Clear the flask session
	session.clear()
	#Return back to home page
	return flask.redirect(flask.url_for('show_index'))