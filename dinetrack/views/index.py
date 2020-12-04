
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
		cur = cur.execute(query)
		db_password = cur.fetchall()[0][0]
		if not db_password:
			flask.abort(403)
		if not password == db_password:
			flask.abort(403)
		session['username'] = username
		print('User logged in!')
		return flask.redirect(flask.url_for('show_home'))
		#Load some other page to show
	return flask.render_template("index.html")

@dinetrack.app.route('/home/')
def show_home():
	return flask.render_template("home.html", username=session['username'])

@dinetrack.app.route('/about/')
def show_about():
	return flask.render_template("about.html", username=session['username'])

@dinetrack.app.route('/meals/', methods=['POST', 'GET'])
def show_meals():
	if request.method == 'POST':
		date = request.form['date']
		calorie_inputs = request.form.getlist('calorie')
		username = session['username']
		db = get_db()
		cur = db.cursor()

		for c_input in calorie_inputs:
			print(date)
			query = "INSERT INTO meals(username, date, calories) VALUES ('{}', '{}', '{}')".format(username, date, c_input)
			cur.execute(query)
			db.commit()

	return flask.render_template("meals.html", username=session['username'])

@dinetrack.app.route('/tip/')
def show_tip():
	return flask.render_template("tip.html", username=session['username'])

@dinetrack.app.route('/stats/', methods=['POST', 'GET'])
def show_stats():
    context={"username": session['username'], "calories":-1}
    if request.method == 'POST':
        startDate = request.form['start']
        endDate = request.form['end']
        username = session['username']
        db = get_db()
        cur = db.cursor()

        query = "SELECT calories FROM meals WHERE username = '{}' AND date BETWEEN '{}' AND '{}'".format(username, startDate, endDate)
        cur = cur.execute(query)
        calorieList = cur.fetchall()
        total = 0
        for cal in calorieList:
            total += cal[0]
		
        context = {"username": username, "calories":total, "startDate":startDate, "endDate":endDate}
    return flask.render_template("stats.html", **context)

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
		return flask.redirect(flask.url_for("show_home"))
	return flask.render_template("create.html")

#Call this url for any logout link
@dinetrack.app.route('/accounts/logout/', methods=['POST', 'GET'])
def logout():
	#Clear the flask session
	session.clear()
	#Return back to home page
	return flask.redirect(flask.url_for('show_index'))
