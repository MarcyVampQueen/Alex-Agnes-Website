##
## For importing data from the database
##

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc


######## Set up DB ########
engine = create_engine("sqlite:///static/agnesShows.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

def getData():
    return 0

