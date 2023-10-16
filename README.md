# Climate Analysis in Honolulu, Hawaii Using Advance SqlAlchemy

This project provides a climate analysis and data exploration of Honolulu, Hawaii, using Python, SQLAlchemy, Pandas, and Matplotlib. By exploring the climate data, travelers and enthusiasts can get a better understanding of the precipitation and temperature trends in the region.

## 📚 Table of Contents

- [Overview](#overview)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Features](#features)


## 🔍 Overview

The climate data analysis provides insights into:
- Precipitation trends over the past year.
- Summary statistics for precipitation data.
- The total number of weather stations.
- The most active weather stations and their respective temperature observations.

## 🛠 Installation & Setup

1. Ensure you have Python, Pandas, SQLAlchemy, Matplotlib, and Jupyter Notebook installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/data-analyst05/sqlalchemy_project.git
## Project Setup

Navigate to the project directory and ensure the `hawaii.sqlite` database file is present in the `/Resources` directory.

## 🚀 Usage

1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
2. Open the climate_starter.ipynb file.
3. Execute the cells in sequence to visualize the results.
4. Adjust queries and plots as needed for further exploration.


## ✨ Features

- **Precipitation Analysis:** Retrieves the last 12 months of precipitation data, visualizing the results with a line plot.

- **Station Analysis:** Calculates and visualizes statistics on the total number of weather stations, their activity levels, and temperature observations for the most active station.

- **Histogram of Temperature Observations:** Provides a histogram of the last year's temperature observations for the most active station, allowing for a clear understanding of temperature distribution.


# PART 2

## Climate Analysis Flask API

This Flask-based API provides an interface to query climate data stored in an SQLite database.

## 🌦 Features

- **Precipitation Data**: Retrieve the last year's precipitation information.
- **Station Data**: Access information about various weather stations.
- **Temperature Observations**: Fetch temperature observations for the most active station over the last year.
- **Temperature Statistics**: Compute minimum, average, and maximum temperatures for a specified date range.

## 🛠 Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy

### Installation

1. **Install Dependencies**:

   ```bash
   pip install Flask SQLAlchemy

## 📦 Database Setup

Ensure your SQLite database file is placed in the project directory. Update the `DATABASE_URI` in the Flask app to reflect the correct path and name of your SQLite file.

## 🚀 Usage

### Running the Flask App

    ```bash
    python app.py

## 🌐 API Endpoints

- **/** - Home, displays all available routes.
- **/api/v1.0/precipitation** - Fetches last year's precipitation data.
- **/api/v1.0/stations** - Provides a list of all weather stations.
- **/api/v1.0/tobs** - Retrieves temperature observations for the most active station over the last year.
- **/api/v1.0/<start>** - Calculates temperature statistics (TMIN, TAVG, TMAX) from the start date to the end of the dataset.
- **/api/v1.0/<start>/<end>** - Computes temperature stats (TMIN, TAVG, TMAX) between specified start and end dates.




