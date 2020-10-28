from flask import Flask,jsonify
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


##################################################
# Database Setup
###################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#save reference to table measurement
Measurement = Base.classes.measurement

#save reference to table station
Station = Base.classes.station

#########################################################
# Flask Setup
#######################################################
app = Flask(__name__)
##########################################################
# Flask Routes
#########################################################

@app.route("/")
def welcome():
    """List all available api routes"""
    return(
    " f" Honolulu Weather data:<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

   results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-24").\
        all()

    session.close()

# Convert to Dictionary
    all_prcp = []
    for date,prcp  in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
               
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)


# return Json list of stations

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations"""
    # Query all Stations
    results = session.query(Station.station).\
                 order_by(Station.station).all()

session.close()

# return station list
 # Query all Stations
    results = session.query(Station.station).\
                 order_by(Station.station).all()

    session.close()

if __name__ == "__main__":
    app.run(debug=True)
