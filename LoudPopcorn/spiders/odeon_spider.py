from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urlparse
from geopy import geocoders
from LoudPopcorn.items import OdeonCinemaItem
from LoudPopcorn.helper_functions import GetOdeonId

class DmozSpider(BaseSpider):
    name            = "odeon"
    allowed_domains = ["odeon.co.uk"]
    start_urls      = ["http://www.odeon.co.uk/fanatic/film_times/"]                      
    domain_name     = "odeon.co.uk"
    g               = geocoders.Google(domain='maps.google.co.uk')
    y               = geocoders.Yahoo('NbD5Hw6e')
    items           = []
    chain           = "Odeon"

    def parse(self, response):
        hxs            = HtmlXPathSelector(response)
        cinema_urls    = hxs.select('//select[@id="cinema"]').select('//option').select('attribute::value').extract()
        
        for url in cinema_urls:
            link   =  urlparse.urljoin(response.url, url.strip())
            yield Request(link, callback=self.parse_cinema)

    def parse_cinema(self, response):
        
        hxs     = HtmlXPathSelector(response)

        item    = self.GetCinemaAddress(hxs, response)
        item    = self.GetTimeListings(hxs, response, item)

        yield item


    def GetCinemaAddress(self, hxs, response):

        address        = hxs.select('//div[@class="selectedCinema"]').select('child::p[position()=3]').select('child::br').extract()
        address_list   = []
        
        for i in range(6):
            try:
                address_list.append(address[i].replace('<br>','').replace('13;','').strip('\n\t>&#;,.'))
            except:
                pass

        try:
            item = OdeonCinemaItem()
            address, (lat, lng) = self.y.geocode(' '.join(address_list))
        
        except ValueError:
            
            address = None
            lng     = None
            lat     = None

        print response.url
        
        item['chain_id']    = GetOdeonId(response.url)
        item['name']        = address_list[0]
        item['address']     = address
        item['lng']         = lng
        item['lat']         = lat

        self.items.append(item)

        return item

    def GetTimeListings(self, hxs, response, item):
        films       = hxs.select('//div[@class="filmdiv"]')
        films_dict  = {}
        
        for film in films:
            film_id     = film.select('attribute::id').extract()[0]
            film_name   = film.select('div[contains(@class,"filmblock")]/div[@class="rightside"]/div[@class="filminfos"]').select('child::h1').select('child::a//text()').extract()[0]
            days        = film.select('div[contains(@class,"timeslisting") and contains(@class, "fRegular")]/div[contains(@class,"dayline")]')
            
            days_dict = {}
            for day in days:
                
                day_name        = day.select('div[@class="day"]/span//text()').extract()[0]
                day_times       = day.select('div[@class="showingtimes"]/span')
                
                day_times_list  = []
                for time in day_times:
                    time_link   = time.select('a/@href').extract()[0]
                    film_time   = time.select('a//text()').extract()[0]
                    day_times_list.append([film_time, time_link])

                days_dict[day_name] = day_times_list

            films_dict[film_name]   =  [film_id, days_dict]

        item['times']       = films_dict

        return item

