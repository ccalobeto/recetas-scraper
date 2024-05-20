## recetas

This personal project do :
- scrape https://www.recetasgratis.net/
- prepare data with python
- make some visualizations in python
- predict the cuisine from ingredients used (next level)

if you want to run the spider, go to the folder scraperecetas
and run: **scrapy crawl recetaspider**. The scraped file will
be in data/raw/recetas.json.

## Advanced scraping tools
### 1. Rotating Proxies
use a list of paid ip proxies.
#### 1.1 Install Rotating proxies
`pip install crapy-rotating-proxies` 
#### 1.2 Edit configuration in settings.py

`DOWNLOADER_MIDDLEWARES = { 
  'rotating_proxies.middlewares.RotatingProxyMiddleware': 300,
  'rotating_proxies.middlewares.BanDetectionMiddleware': 301,
  ...
}
ROTATING_PROXI_LIST_PATH = 'proxies.txt'
`

### 2.a Using agents in settings.py
#### 1.1. Install agents
`pip install scrapy-fake-useragent`

#### 1.2 Edit settings.py

`DOWNLOADER_MIDDLEWARES = { 
  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
  'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
  'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
  'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

### 2.b Using agents in the spider

#### Edit settings.py
Document # `DOWNLOADER_MIDDLEWARES`

### Edit recetaspider.py
`
 agent = UserAgent()
    custom_settings = {
        'USER_AGENT': agent.random
    }
`




