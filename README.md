# Explore Bikeshare

## 1. Overview

This python script is written with the motive of exploring descriptive statistics for bike sharing system in three populous US cities; New York City, Chicago, and Washington. The script also provides some level of interactivity where users can control filters applied to the data.

## 2. Getting Started

### 2.1. Dependencies

This script uses Python 3.x. No extra libraries are necessary beyond the Anaconda distribution. It uses **NumPy** and **Pandas** libraries. It also uses **time** and **datetime** from python standard library.

### 2.2. Installation

Clone this repository `git clone https://github.com/1992Sahar/explore-bikeshare.git`

Then run from any python IDE using `python bikeshare.py`

## 3. Content

### 3.1. Files

*   `bikeshare.py`: Python script that loads in dataset and performs necessary calculations according to user input in an interactive experience.
*   `new_york_city.csv`,`chicago.csv`,`washington.csv`: Datasets used as a source for providing descriptive statistics. Not pushed to repo due to large size.

### 3.1. Data

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns: `Start Time`, `End Time`, `Trip Duration`, `Start Station`, `End Station`, and `User Type`. The Chicago and New York City files also have the following two columns: `Gender` and `Birth Year`.

![First 10 rows of new_york_city.csv file](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)
First 10 rows of `new_york_city.csv` file. Image courtesy of Udacity.

### 3.2. Statistics Computed

The script provides the following statistics from the bike share data:

*   Popular times of travel
    *   Most common month
    *   Most common day of week
    *   Most common hour of day
*   Popular stations and trip
    *   Most common start station
    *   Most common end station
    *   Most common trip from start to end
*   Trip duration
    *   Total travel time
    *   Average travel time
*   User info
    *   Counts of each user type
    *   Counts of each gender (if applicable)
    *   Earliest, most recent, most common year of birth (if applicable)

## 4. Acknowledgements

This python script is written to be submitted as a project for [Udacity Programming for Data Science with Python Nanodegree](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104). Many thanks for the mentorship and guidance.
