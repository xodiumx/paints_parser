import os

from dotenv import load_dotenv

load_dotenv()


BOT_NAME = "test_task"

SPIDER_MODULES = ['crawls.spiders']
NEWSPIDER_MODULE = 'crawls.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "test_task.middlewares.TestTaskSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "test_task.middlewares.TestTaskDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'crawls.pipelines.OrdernnPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


# DB settings

DATABASE = {
   'DB_HOST':  os.getenv('DB_HOST'),
   'DB_PORT':  os.getenv('DB_PORT'),
   'DB_NAME':  os.getenv('DB_NAME'),
   'DB_USER':  os.getenv('DB_USER'),
   'DB_PASS':  os.getenv('DB_PASS'),
}


# ORDER_NN site constants

ORDERNN_CONST = {
    'xpath_categories': '//a[text()="Краски и материалы специального назначения" or text()="Краски для наружных работ" or text()="Лаки"]/@href',
    'xpath_item_urls': '//a[@itemprop="url"]/@href',
    'xpath_pagination': '//div[@id="all-product"]/text()',
    'count_items': 30,
    'xpath_name': '//h1/text()',
    'xpath_price': '//span[@itemprop="price"]/text()',
    'xpath_description': '//div[@id="block-description"]//text()',
    'endpoint_characterstics': 'https://order-nn.ru/local/ajax/kmo/getCharacterItems.php?type=character&style=element&items=',
    'xpath_characterstics': '//table[@class="table table-striped table-character"]/tr',
    'xpath_character_key': './/td[@class="table-character-text"]/text()',
    'xpath_character_value': './/td[@class="table-character-value"]/text()'
}

# Save data
FEEDS = {
    'ordernn_%(time)s.json': {
        'format': 'json', 
        'encoding': 'utf-8', 
        'indent': 4
    },
    'ordernn_%(time)s.csv': {
        'format': 'csv',
        'fields': ['name','price','url','characteristics']
    }
}

# LOGS

LOG_LEVEL = 'ERROR'