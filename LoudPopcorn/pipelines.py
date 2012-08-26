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
from db_setup import Cinema, Film, Showing

class ProcessCinemaPipeline(object):
	def __init__(self):
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)
		engine = create_engine('sqlite:///test.db', echo=True)
		Session = sessionmaker(bind=engine)


	def spider_opened(self, spider):
		spider.session = Session()

	def spider_closed(self, spider):
		pass

    def process_item(self, item, spider):
    	if type(item) == OdeonCinemaItem:
    		pass # pipline to process odeon item chec k if it is in the db and add if its not.
    	else:
        	return item

class ProcessFilmTimes(object):
	def process_item(self,item,spider): 
		if type(item) == OdeonFilmTimesItem:
			times 		= item['times']
			
			for film, data in times.items():
				film_id = data[0]
				days 	= data[1]
		
		else:
			return item


	def GetFilmId(self, film):
		# takes the title of the film and returns the our database id of
		film = self.CleanFilmName(film)


	def CleanFilmName(film_name):
		'''Pipline to clean film names'''
		
		unwanted_list = ["-", ":"]
		for i in in unwanted_list:
			film_name = film_name.replace(i,"")
		film_name_split = film_name.strip().split()
		
		if "3D" in film_name_split:
			film_name_split.remove("3D")
			film_name_split.append("3D") #use convention of 3d at end
		elif "2D" in film_name_split:
			film_name_split.remove("2D")

		clean_film = " ".join(film_name_split)

class LoudpopcornPipeline(object):
    def process_item(self, item, spider):
        return item
