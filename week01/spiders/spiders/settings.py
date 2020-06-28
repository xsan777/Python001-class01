# Scrapy settings for spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiders'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'maoyan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'uuid_n_v=v1; uuid=905CCBE0B93411EA909D9FF2C00A78C3DA1C671C8ED34CCD9C8C4CF66D10CB55;\
     _csrf=0bf1e3c753ae9e2fc4dd023a222a068e472277f2aaaf9779c68deadc3f737167; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593344600;\
      _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172fabd2830c8-0fc66c925d0951-366b4108-1fa400-172fabd2830c8; \
      _lxsdk=905CCBE0B93411EA909D9FF2C00A78C3DA1C671C8ED34CCD9C8C4CF66D10CB55; mojo-uuid=3af7560acfd7a2808b4082a90a08b209; \
      mojo-session-id={"id":"d570e12bf5dced914d00a7a600df6812","time":1593347080438}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593347576;\
       mojo-trace-id=3; __mta=146579339.1593344600955.1593347081191.1593347576230.3; _lxsdk_s=172fae30056-845-923-7c3%7C%7C6',
    'Host': 'maoyan.com',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'spiders.middlewares.SpidersDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'spiders.pipelines.SpidersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
