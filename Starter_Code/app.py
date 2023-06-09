# Import the dependencies.
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reflect Tables into SQLAlchemy ORM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python SQL toolkit and Object Relational Mapper\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func, inspect, Date, Float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create engine to hawaii.sqlite\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
  "Base=automap_base()\n",
    "\n",
       
# reflect the tables
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['measurement', 'station']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [

# Save references to each table
    "measurement = Base.classes.measurement\n",
    "station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [

# Create our session (link) from Python to the DB
    "session=Session(engine)"
   ]
  },

#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
