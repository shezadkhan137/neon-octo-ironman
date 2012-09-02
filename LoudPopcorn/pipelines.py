# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
#################
###### times --- dictionary with key [film name] and data tuple of film id and dictionary [weekday] = times


from LoudPopcorn.items import *
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Cinema, Film, Showing, Locale
from sqlalchemy import and_
import datetime
from geopy import geocoders
from geopy import distance

class ProcessCinemaPipeline(object):
	def __init__(self):
		engine = create_engine('sqlite:///test.db', echo=False)
		Session = sessionmaker(bind=engine)
		self.session = Session()
		self.y = geocoders.Yahoo('NbD5Hw6e')


	def process_item(self, item, spider):
		cinema_name 	= item['name']
		cinema_chain_id = item['chain_id']
		cine_test = self.session.query(Cinema).filter(and_(Cinema.name==cinema_name, Cinema.chain_id==cinema_chain_id )).first()
		if  cine_test is None:
			new_cinema 			= Cinema(name=cinema_name)
			new_cinema.chain_id = cinema_chain_id
			new_cinema.address 	= item['address']
			new_cinema.lng 		= item['lng']
			new_cinema.lat 		= item['lat']
			new_cinema.chain 	= spider.chain
			self.session.add(new_cinema)
			for locale in self.session.query(Locale).all():
				if distance.distance((new_cinema.lat,new_cinema.lng), (locale.lat, locale.lng)).miles <= 3:
					locale.cinemas.append(new_cinema)
					self.session.add(locale)
			self.session.commit()
		return item

class ProcessFilmTimes(object):
	def __init__(self):
		engine = create_engine('sqlite:///test.db', echo=False)
		Session = sessionmaker(bind=engine)
		self.session = Session()

	def process_item(self,item,spider): 
		cinema_chain_id = item['chain_id']
		cinema = self.session.query(Cinema).filter(Cinema.chain_id==cinema_chain_id).first()
		self.session.add(cinema)
		times = item['times']
		
		for film_name, data in times.items():
			film = self.GetFilmId(film_name)
			self.CheckFilmInCinema(film,cinema)
			film_id = data[0]
			days = data[1]
			for day, showing_times in days.items():
				t = self.ProcessShowingTime(day, showing_times)
				self.AddShowings(t, cinema, film)

		self.session.close()
		return item

	def AddShowings(self, showing_times, cinema, film):
		pass #add showings to dbs
		for showing_time in showing_times:
			tmp_showing = Showing(time=showing_time[0], film=film, cinema=cinema, link=showing_time[1])
			if tmp_showing not in self.session.query(Showing).all():
				self.session.add(tmp_showing)

		self.session.commit()

	def ProcessShowingTime(self, day, showing_times):
		weekdays = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6}
		weekday = weekdays[day]
		today_date = datetime.date.today()
		showing_day = today_date+datetime.timedelta(weekday-today_date.weekday())
		showing_list = []
		for showing_time, link in showing_times:
			h, m = showing_time.split(":")
			showing_datetime = datetime.datetime.combine(showing_day,datetime.time(hour=int(h), minute=int(m)))
			showing_list.append((showing_datetime, link))

		return showing_list
	

	def CheckFilmInCinema(self, film, cinema):
		if film in cinema.films:
			pass
		else:
			cinema.films.append(film)
			self.session.commit()


	def GetFilmId(self, film):
		# takes the title of the film and returns the our database id of
		film = self.CleanFilmName(film)
		film_exists = self.session.query(Film).filter(Film.name==film).first()
		if type(film_exists) == list:
			film_exists = film_exists[0]
		if film_exists is None:
			new_film = Film(name=film, release_date=datetime.datetime.now(), showing=True)
			film_exists = new_film
			self.session.add(film_exists)
			self.session.commit()

		return film_exists

	def CleanFilmName(self, film_name):
		'''Pipline to clean film names'''
		
		unwanted_list = ["-", ":"]
		for i in unwanted_list:
			film_name = film_name.replace(i,"")
		film_name_split = film_name.strip().split()
		
		if "3D" in film_name_split:
			film_name_split.remove("3D")
			film_name_split.append("3D") #use convention of 3d at end
		elif "2D" in film_name_split:
			film_name_split.remove("2D")

		clean_film = " ".join(film_name_split)

		return clean_film
