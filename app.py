# DABC Module 9
# 2022-08-07
# LaStella

# Create a New Python File and Import the Flask Dependency
# Create a new Python file called app.py. You should create this file in VS Code.
# Once the Python file is created, we can import the dependency we need. 
# This dependency will enable your code to access all that Flask has to offer.
# To import the Flask dependency, add the following to your code:
from flask import Flask


# We're now ready to create a new Flask app instance. 
# "Instance" is a general term in programming to refer to a 
# singular version of something. Add the following to your 
# code to create a new Flask instance called app:
app = Flask(__name__)
# This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code 
# is being run from the command line or if it has been imported 
# into another piece of code. Variables with underscores 
# before and after them are called magic methods in Python.


# First, we need to define the starting point, also known as 
# the root. To do this, we'll use the function @app.route('/'). 
# Add this to your code now.
@app.route('/')
# Notice the forward slash inside of the app.route? 
# This denotes that we want to put our data at the 
# root of our routes. The forward slash is commonly 
# known as the highest level of hierarchy in any computer system.

def hello_world():
    return 'Hello world'

#  Windows: Start by opening up Anaconda Powershell. 
# Once you've done that, enter this command.
    # set FLASK_APP=app.py
# Now let's run our Flask app. To do this, type the 
# following command in your command line and press Enter:
    # flask run

# When you run this command, you'll notice a line that says "Running on" followed by an address. This should be your localhost address and a port number.

# IMPORTANT
# A port number is essentially the endpoint of a given program 
# or service. Any Flask application you create can have 
# whatever port number you would like, but the most common is 5000.

# Copy and paste your localhost address into your web browser. 
# Generally, a localhost will look something like this, 
# for context. 
# localhost:5000

# http://127.0.0.1:5000/


# New route test:
# @app.route('/zebra')



