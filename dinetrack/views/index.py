
import os
import flask
import dinetrack
from dinetrack.database import get_db, close_connection
from flask import session
from flask import request
#import googlemaps
import urllib.request
import json
import datetime
import random
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

@dinetrack.app.route('/home/', methods=['POST', 'GET'])
def show_home():
    context = {}
    if request.method == 'POST':
        location = request.form['location']
        context['location'] = location
        split_location = location.split(" ")
        location = ""
        for word in split_location:
            location += word + "+"
        location = location[:-1]
        print(location)
        construct_url= "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+"+location+"&key=AIzaSyBnRQa8lUcBihRuSSdL0Cy8fGMVi09ZUsc"
        print(construct_url)
        with urllib.request.urlopen(construct_url) as url:
            data = json.loads(url.read().decode())
        results = data["results"]
        #print(results)
        context['username'] = session['username']
        context['restaurants'] = results
        return flask.render_template("location.html", **context)
    # code for loading stuff
    construct_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+University+of+Michigan+Ann+Arbor&key=AIzaSyBnRQa8lUcBihRuSSdL0Cy8fGMVi09ZUsc"
    #print(construct_url)
    with urllib.request.urlopen(construct_url) as url:
        data = json.loads(url.read().decode())
    results = data["results"]
    print("Hello:", results[0]["opening_hours"]["open_now"])
    #print(results)
    context['username'] = session['username']
    context['restaurants'] = results
    return flask.render_template("home.html", **context)

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
        finalStartDate = datetime.datetime.strptime(startDate,'%Y-%m-%d').strftime('%B %d, %Y')
        finalEndDate = datetime.datetime.strptime(endDate,'%Y-%m-%d').strftime('%B %d, %Y')

        funFacts = ["Canadians spend about 60 minutes a day on eating, while the French spend about 133 minutes a day.",
        "Milk is the #1 source of riboflavin in the Canadian diet. Riboflavin keeps skin, eyes and nerves healthy and releases energy in cells.",
        "Fluid needs vary depending on your age and gender. Teens and adults need anywhere between 8 and 13 cups of fluid each day. Water is great, but milk, juice, soup and anything else you drink also count as fluid.",
        "Broccoli is a source of calcium. You can get 50 mg of calcium from a 3/4 cup (175 mL) portion. Adults aged 19–50 need 1000 mg of calcium every day.",
        "Eggs contain the highest quality food protein known. All parts of an egg are edible, including the shell which has a high calcium content.",
        "The mushroom is the only non-animal natural source of vitamin D.",
        "The world has more than 50,000 edible plants, yet just three commodity crops such as rice, maize, and wheat, provide 60% of the plant-derived calories we eat.",
        "Broccoli, parsley, brussel sprouts, and red bell peppers all contain more vitamin C per 100g serving than oranges. Chili peppers contain 400% more.",
        "There is a fruit by the name of Black Sapote or 'chocolate pudding fruit' which tastes like chocolate pudding and is actually low in fat and has about 4 times as much vitamin C as an orange.",
        "Potatoes have a bad reputation, but are actually highly beneficial to your health. They are packed with Vitamin C, Potassium, Fiber, Vitamin B6 and kukoamines which help aid in lowering blood pressure.",
        "Too much of a spice can be a bad thing, and nutmeg is no exception. If you have two or more teaspoons of the spice, it can actually cause hallucinations!",
        "Next time you're feeling dehydrated and don't feel like drinking water, try snacking on a cucumber; it's 96 percent water.",
        "Peanuts are actually an ingredient in dynamite. They have oil in them called glycerol that's used to create nitroglycerin, a key ingredient in dynamite.",
        "The stickers that are placed on our favourite fruit are actually fine to eat. Now you don’t have to freak out when you accidentally take a chomp of one!",
        "The most stolen food in the world is in fact cheese. Around 4% of ALL the cheese made in the world gets stolen. There's even a black market of stolen cheeses, but we didn't tell you that.",
        "The oily fibrous materials used to transport pistachio nuts can cause them to break out in flames! Exercise caution whenever you pass a big mound of pistachio nuts.",
        "There was a lawsuit that took place trying to prove that Pringles are not really potato chips.",
        "Arachibutyrophobia is the fear of getting peanut butter stuck to the top of your mouth. (Yes, this is a real fear.)",
        "It may not taste as good as Yoplait or frozen yogurt, BUT greek yogurt has DOUBLE the amount of protein in it than all those other leading brands. So, walk past the Go-Gurts and grab the Chobani (it's worth it).",
        "Honey is the only food that has an eternal shelf life. It will never rot or go bad as long as you live.",
        "Canned peaches were the first ever fruit to be consumed on the moon.",
        "Back in 1928, machine-sliced bread was first introduced, changing the world as we knew it. But only 15 years later, in 1943, it was banned by the FDA for using too much plastic that could be used for the war effort instead. The ban only lasted three months, though, as the public outcry it caused was too great.",
        "The most expensive pizza in the world costs $12,000. That’s because it takes 72 hours to make, and it can only be made in your home by 3 Italian chefs. The pizza is topped with 3 types of caviar, bufala mozzarella, lobster from Norway and Cilento, and pink Australian sea salt.",
        "Back in the early 1800’s, people thought tomatoes had medicinal qualities. One doctor claimed they could treat diarrhea and indigestion, so he made a recipe for a type of tomato ketchup which then became a pill.",
        "White chocolate isn’t chocolate. Its name is deceiving, because white chocolate doesn’t have any components of regular chocolate. It’s really just a mixture of sugar, milk, vanilla, lecithin, and cocoa butter.",
        "In Russia, until 2013, beer and other alcohol under 10% ABV was classified as a soft drink! Until then, and even still today, it was common for people to drink beer in the streets and parks as commonly as you would see soda."
        ]
        fact = random.choice(funFacts)
        message = ""
        if (total == 0):
            message = "Are you sure you have been recording your meals?"
        else:
            message = "Nice! Keep recording your calories to consistently track your progress."
        context = {"username": username, "calories":total, "startDate":finalStartDate, "endDate":finalEndDate, "funFact":fact, "message":message}
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
