from scrapy import Spider, Request
import re
import json
from utils import time_str2iso_format


class NewsCrawler(Spider):
    def __init__(self, name=None, **kwargs):
        self.allowed_domains = [kwargs.get('domain')]
        self.start_urls = kwargs.get('start_urls')
        self.xpath = kwargs.get('xpath')
        super(NewsCrawler, self).__init__(name, **kwargs)

    def start_requests(self):
        for start_url in self.start_urls:
            yield Request(url=start_url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath(self.xpath['news_link']).getall()

        for url in urls:
            yield Request(url=response.urljoin(url), callback=self.parse_content)

        next_page = response.xpath(self.xpath['next_page']).get()
        if next_page is not None:
            yield Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_content(self, response):
        pass


class VNExpress(NewsCrawler):
    custom_settings = {
        'FEED_URI': 'data/vnexpress.jsonl'
    }

    def parse_content(self, response):
        time = response.xpath(self.xpath['time']).get()
        title = response.xpath(self.xpath['title']).get()
        description = response.xpath(self.xpath['description']).get()
        content = [paragraph for paragraph in [p.strip() for p in response.xpath(self.xpath['content']).getall()] if
                   paragraph != '']
        author = ''.join(response.xpath(self.xpath['author']).getall())
        tags = [tag.strip() for tag in response.xpath(self.xpath['tags']).getall()]

        article_id = re.findall(r'.+-(\d+)\.htm', response.request.url)
        data = {'time': time_str2iso_format(time.strip()) if time is not None else '',
                'title': title.strip() if title is not None else '',
                'description': description.strip() if description is not None else '',
                'content': content,
                'author': author.strip() if author is not None else '',
                'tags': tags,
                'url': response.request.url}
        # if len(article_id) > 0:
        #     yield Request(url=self.get_comment_url(article_id[0]), callback=self.parse_comments,
        #                   meta={'data': data})
        if data['title'] and data['description'] and data['content']:
            yield data

    def parse_comments(self, response):
        comments_obj = json.loads(response.text)

        comments = [comment['content'] for comment in comments_obj['data']['items']] if 'items' in comments_obj[
            'data'] else []
        yield {**response.meta['data'],
               'comments': comments}

    @staticmethod
    def get_comment_url(article_id):
        return f"https://usi-saas.vnexpress.net/index/get?offset=0&limit=24&sort=like&is_onload=1&objectid={article_id}&objecttype=1&siteid=1000000"


class News24h(NewsCrawler):
    custom_settings = {
        'FEED_URI': 'data/24h.jsonl'
    }

    def parse_content(self, response):
        time = response.xpath(self.xpath['time']).get()
        title = response.xpath(self.xpath['title']).get()
        description = response.xpath(self.xpath['description']).get()
        content = [paragraph for paragraph in [p.strip() for p in response.xpath(self.xpath['content']).getall()] if
                   paragraph != '']
        author = ''.join(response.xpath(self.xpath['author']).getall())

        data = {'time': time_str2iso_format(time.strip(), is_24h_format=False) if time is not None else '',
                'title': title.strip() if title is not None else '',
                'description': description.strip() if description is not None else '',
                'content': content,
                'author': author.strip(),
                'url': response.request.url}

        if data['title'] and data['description'] and data['content']:
            yield data
