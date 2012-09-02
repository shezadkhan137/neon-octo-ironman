# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class OdeonCinemaItem(Item):
	name = Field()
	address = Field()
	lng = Field()
	lat = Field()
	chain_id = Field()
	times = Field()