import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)                   #This is to reflect on the SQLite Database



Measurement = Base.classes.measurement                 # Create and save our references for Measurement and Station
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)                                  #This will create a Flask application called “app.”

# Create a New Flask App Instance
# define the Route) starting point, also known as the root
@app.route('/')
def hello_world():
	return 'Hello world'


@app.route("/")                                         # Set up our root or route for welcome
def welcome():                                          # Create a function welcome
	return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

                                   # Variable inside of Flask() function(magic methods in Python)

@app.route("/api/v1.0/precipitation")                               # 9.5.3 Build precipitation route
def precipitation():                                                # Create a function for precipitation
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)        # Calculates the date one year ago from the most recent date in the database
    precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}            # Create a dictionary that uses date as key: and precipitation as value
    return jsonify(precip)                                           # Jsonify() is a function that converts the dictionary to a JSON file


@app.route("/api/v1.0/stations")
def stations():                                                     # Create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()                  # Unravel our results into a one-dimensional array. Use np.ravel(), results as parameter
    stations = list(np.ravel(results))                              # Convert to a list using list() function
    return jsonify(stations=stations)                               # Jsnify() and return as JSON


@app.route("/api/v1.0/tobs")
def temp_monthly():                                                 # Create a function for monthly temperature
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)       # Query the primary station for all the temperature observations from the previous year

    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))                                 # Unravel the results into a one-dimensional array and convert that array into a list
    return jsonify(temps=temps)


@app.route("/av1.0/temp/pi/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
		filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
	     filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

################################################################################
#                       Module 9 Challenge                                     # 
#                                                                              # 
################################################################################

@app.route("/api/v1.0/precipitation")                               # 9.5.3 Build precipitation route
def precipitation():                                                # Create a function for precipitation
    prev_year = dt.date(2017, 6, 1) - dt.timedelta(days=365)        # Calculates the date one year ago from the most recent date in the database
    precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}            # Create a dictionary that uses date as key: and precipitation as value
    return jsonify(precip)                  


@app.route("/api/v1.0/precipitation")                               # 9.5.3 Build precipitation route
def precipitation():                                                # Create a function for precipitation
    prev_year = dt.date(2017, 12, 1) - dt.timedelta(days=365)        # Calculates the date one year ago from the most recent date in the database
    precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}            # Create a dictionary that uses date as key: and precipitation as value
    return jsonify(precip)                  


@app.route("/api/v1.0/tobs")
def temp_June():                                                # Create a function for monthly temperature
    prev_year = dt.date(2017, 6, 1) - dt.timedelta(days=365)    # Query the primary station for all the temperature observations from the previous year

    results = session.query(Measurement.tobs,)  
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))                             # Unravel the results into a one-dimensional array and convert that array into a list
    return jsonify(temps=temps)


@app.route("/api/v1.0/tobs")
def temp_December():                                                # Create a function for monthly temperature
    prev_year = dt.date(2017, 12, 1) - dt.timedelta(days=365)    # Query the primary station for all the temperature observations from the previous year

    results = session.query(Measurement.tobs,)  
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))                             # Unravel the results into a one-dimensional array and convert that array into a list
    return jsonify(temps=temps)



@app.route("/av1.0/temp/pi/2016-06-01")
@app.route("/api/v1.0/temp/2016-06-01/2016-06-30")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
		filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
	     filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)




@app.route("/av1.0/temp/pi/2016-06-01")
@app.route("/api/v1.0/temp/2016-06-01/2016-06-30")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
		filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
	     filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)




@app.route("/av1.0/temp/pi/2016-06-01")
@app.route("/api/v1.0/temp/2016-06-01/2016-06-30")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
		filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
	     filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)




@app.route("/av1.0/temp/pi/2016-12-01")
@app.route("/api/v1.0/temp/2016-12-01/2016-12-31")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
		filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
           filter(Measurement.date >= start).\
	     filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)



















if __name__ == '__main__':
    app.run()