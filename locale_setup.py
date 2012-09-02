from sqlalchemy.orm import sessionmaker
from LoudPopcorn.db_setup import *
from sqlalchemy.orm import sessionmaker
london = Locale(name="London Zone 1")
Session = sessionmaker(bind=engine)
session = Session()
session.add(london)
session.commit()
from geopy import geocoders
y               = geocoders.Yahoo('NbD5Hw6e')
_ , (lat, lng) = y.geocode("EC1V 9AQ")
london.lat = lat
london.lng = lng
london.radius = 3
session.commit()

from termcolor import colored, cprint

h = "Hello"

text = colored('OK', 'green',)
print("%s["%h+text+"]")

