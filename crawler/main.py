from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawler import VNExpress, News24h
from settings import *

if __name__ == '__main__':
    settings = get_project_settings()
    settings.update(SETTINGS)

    process = CrawlerProcess(settings)

    configure_logging()
    process.crawl(VNExpress, name='vnexpress', domain='vnexpress.net', start_urls=VNEXPRESS_START_URLS,
                  xpath=VNEXPRESS_XPATH)
    # process.crawl(News24h, name='24h', domain='24h.com.vn', start_urls=VN24H_START_URLS, xpath=VN24H_XPATH)
    process.start()
