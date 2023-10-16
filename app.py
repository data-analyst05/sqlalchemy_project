# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import numpy as np

#################################################
# Database Setup
#################################################

DATABASE_URI = "sqlite:///your_database_file.sqlite"

# Set up the database engine
engine = create_engine(DATABASE_URI)

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
Session = sessionmaker(bind=engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session()
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= func.date('now', '-1 year')).all()
    session.close()

    precipitation_data = {item[0]: item[1] for item in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    session = Session()
    results = session.query(Station.station).all()
    session.close()

    stations = list(np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session()
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= func.date('now', '-1 year')).all()
    session.close()

    temp_observations = {item[0]: item[1] for item in results}
    return jsonify(temp_observations)

@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session()
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    temp_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = Session()
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    temp_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temp_stats)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
