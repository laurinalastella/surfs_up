# Mod 9.5.1

import datetime as dt
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

# NOTE
# When creating routes, we follow the naming convention
#    /api/v1.0/ 
# followed by the name of the route. This convention 
# signifies that this is version 1 of our application. 
# This line can be updated to support future versions 
# of the app as well.

# The welcome route is now defined, so let's try to run our code. 
# You can run Flask applications by using the command below, 
# but you'll need a web browser to view the results.

# Let's start by using the command line to navigate to 
# your project folder. Then run your code:
#   flask run
# After starting the flask application, you'll likely 
# see more text output than you have so far. This is 
# exactly what should happen. The output will probably 
# look like ... a web address where you can view your results:

@app.route("/api/v1.0/precipitation")

def precipitation():
    return

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   return

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   return

# Mod 9.5.3

# "jsonify" our dictionary. Jsonify() is a function that 
# converts the dictionary to a JSON file.

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#    http://127.0.0.1:5000/api/v1.0/precipitation
# Internal Server Error http://127.0.0.1:5000/api/v1.0/





