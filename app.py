# Mod 9.5.1

import datetime as dt
from distutils.log import debug
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# The create_engine() function allows 
# us to access and query our SQLite database file.
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes.
Base = automap_base()
Base.prepare(engine, reflect=True)

# create a variable for each of the 
# classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from 
# Python to our database with the following code:
session = Session(engine)

# To define our Flask app, add the following line of code. 
# This will create a Flask application called "app."
app = Flask(__name__)
# Notice the __name__ variable in this code. This is 
# a special type of variable in Python. Its value 
# depends on where and how the code is run. For 
# example, if we wanted to import our app.py file 
# into another Python file named example.py, the 
# variable __name__ would be set to example.

# IMPORTANT
# All of your routes should go after the 
#     app = Flask(__name__) 
# line of code. Otherwise, your code may not run properly.
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


# When creating routes, we follow the naming convention
#    /api/v1.0/ 
# followed by the name of the route. This convention 
# signifies that this is version 1 of our application. 
# This line can be updated to support future versions 
# of the app as well.

# The welcome route is now defined, so let's try to run our code. 
# You can run Flask applications by using the command below, 
# but you'll need a web browser to view the results.

####################################################################
# Let's start by using the command line to navigate to 
# your project folder. 
# --- Use anaconda powercell prompt, but NOT the PythonData env.
# (base) PS C:\Users\LaStella> cd dabc\DataClass\surfs_up
# (base) PS C:\Users\LaStella\dabc\DataClass\surfs_up> flask run
# Then run your code.
#   flask run
# After starting the flask application, you'll likely 
# see more text output than you have so far. This is 
# exactly what should happen. The output will probably 
# look like ... a web address where you can view your results:
# http://127.0.0.1:5000/

# Route: Precipitatin
# http://127.0.0.1:5000/api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")

# Mod 9.5.3

# "jsonify" our dictionary. Jsonify() is a function that 
# converts the dictionary to a JSON file.

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


# Mod 9.5.4
# Route: Stations
@app.route("/api/v1.0/stations")

# We want to start by unraveling our results into a 
# one-dimensional array. To do this, we want to use 
# the function np.ravel(), with results as our parameter.
# Next, we will convert our unraveled results into a list. 
# To convert the results to a list, we will need to use 
# the list function, which is list(), and then convert 
# that array into a list. Then we'll jsonify the list 
# and return it as JSON. Let's add that functionality 
# to our code:
# NOTE
# You may notice here that to return our list as JSON, 
# we need to add stations=stations. This formats our 
# list into JSON.
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# http://127.0.0.1:5000/api/v1.0/stations
# {
# stations: [
# "USC00519397",
# "USC00513117",
# "USC00514830",
# "USC00517948",
# "USC00518838",
# "USC00519523",
# "USC00519281",
# "USC00511918",
# "USC00516128"
# ]
# }

# Mod 9.5.5

@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Mod 9.5.6

# Our last route will be to report on the minimum, 
# average, and maximum temperatures. However, this 
# route is different from the previous ones in that 
# we will have to provide both a starting and ending 
# date. Add the following code to create the routes:
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")


# We need to add parameters to our stats()function: 
# a start parameter and an end parameter. For now, 
# set them both to None.
# With the function declared, we can now create a 
# query to select the minimum, average, and maximum 
# temperatures from our SQLite database.
# Since we need to determine the starting and ending date, 
# add an if-not statement to our code. This will help 
# us accomplish a few things. We'll need to query our 
# database using the list that we just made. Then, we'll 
# unravel the results into a one-dimensional array and 
# convert them to a list. Finally, we will jsonify our 
# results and return them.
def stats(start=None, end=None):
    sel = [
    func.min(Measurement.tobs), 
    func.avg(Measurement.tobs), 
    func.max(Measurement.tobs)
    ]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
# take note of the asterisk in the query 
# next to the sel list. Here the asterisk 
# is used to indicate there will be multiple 
# results for our query: minimum, average, 
# and maximum temperatures.
# /api/v1.0/temp/2017-06-01/2017-06-30


# Added by instructor:
if __name__=="__main__" :
    app.run(debug=True)



