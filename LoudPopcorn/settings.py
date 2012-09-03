# Scrapy settings for LoudPopcorn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'LoudPopcorn'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['LoudPopcorn.spiders']
NEWSPIDER_MODULE = 'LoudPopcorn.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

LOG_ENABLED = True
LOG_LEVEL = "WARNING"
LOG_FILE = "Scraper.log"

ITEM_PIPELINES = [
    'LoudPopcorn.pipelines.ProcessCinemaPipeline',
    'LoudPopcorn.pipelines.ProcessFilmTimes',
]

