 
import os
import flask
import dinetrack
APP = flask.Flask(__name__)

@dinetrack.app.route('/')
def show_index():
	return flask.render_template("index.html")