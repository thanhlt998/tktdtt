SETTINGS = {
    'LOG_FILE': 'log/file.log',

    # 'DUPEFILTER_CLASS': 'filters.BLOOMDupeFilter',

    'DEPTH_PRIORITY': 1,
    # 'DOWNLOAD_DELAY': 0.1,
    # 'CONCURRENT_REQUESTS': 20,
    'LOG_LEVEL': 'INFO',
    'COOKIES_ENABLED': False,
    'TELNETCONSOLE_PORT': None,
    'FEED_EXPORT_ENCODING': 'utf-8',
    'FEED_EXPORT': 'jsonlines',
    # 'FEED_URI': 'data/vnexpress.jsonl'
}

VNEXPRESS_START_URLS = [
    'https://vnexpress.net/thoi-su',
    'https://vnexpress.net/the-gioi',
    'https://vnexpress.net/kinh-doanh',
    'https://vnexpress.net/giai-tri',
    'https://vnexpress.net/the-thao',
    'https://vnexpress.net/phap-luat',
    'https://vnexpress.net/giao-duc',
    'https://vnexpress.net/suc-khoe',
    'https://vnexpress.net/doi-song',
    'https://vnexpress.net/du-lich',
    'https://vnexpress.net/khoa-hoc',
    'https://vnexpress.net/so-hoa',
    'https://vnexpress.net/oto-xe-may',
    'https://vnexpress.net/y-kien',
    'https://vnexpress.net/tam-su',
    'https://vnexpress.net/cuoi'
]

VNEXPRESS_XPATH = {
    'news_link': "//html/body/section[@class='container']/section[@class='sidebar_1']/article[@class='list_news']/h4/a[1]/@href",
    'time': "//html/body/section[contains(@class,'container')]//section[@class='sidebar_1']/header/span[contains(@class,'time')]/text()",
    'title': "//html/body/section[contains(@class,'container')]//section[@class='sidebar_1']//h1[contains(@class,'title_news_detail')]/text()",
    'description': "//html/body/section[contains(@class,'container')]//section[@class='sidebar_1']//p[contains(@class,'description')]/text()",
    'content': "//html/body/section[contains(@class,'container')]//section[@class='sidebar_1']//article[contains(@class,'content_detail')]//p[not(contains(@style,'text-align'))]/text()",
    'author': "//html/body/section[contains(@class,'container')]//section[@class='sidebar_1']//p[contains(@style,'text-align') or contains(@class,'author')]//text()",
    'tags': "//div[contains(@class,'block_tag')]/h3/a/text()",
    'comments': "",
    'next_page': "//div[@id='pagination']/a[@class='next']/@href"
}

VN24H_START_URLS = [
    'https://www.24h.com.vn/tin-tuc-trong-ngay-c46.html',
    'https://www.24h.com.vn/bong-da-c48.html',
    'https://www.24h.com.vn/tin-tuc-quoc-te-c415.html',
    'https://www.24h.com.vn/thoi-trang-c78.html',
    'https://www.24h.com.vn/thoi-trang-hi-tech-c407.html',
    'https://www.24h.com.vn/kinh-doanh-c161.html',
    'https://www.24h.com.vn/am-thuc-c460.html',
    'https://www.24h.com.vn/lam-dep-c145.html',
    'https://www.24h.com.vn/doi-song-showbiz-c729.html',
    'https://www.24h.com.vn/giai-tri-c731.html',
    'https://www.24h.com.vn/ban-tre-cuoc-song-c64.html',
    'https://www.24h.com.vn/giao-duc-du-hoc-c216.html',
    'https://www.24h.com.vn/the-thao-c101.html',
    'https://www.24h.com.vn/phi-thuong-ky-quac-c159.html',
    'https://www.24h.com.vn/cong-nghe-thong-tin-c55.html',
    'https://www.24h.com.vn/o-to-c747.html',
    'https://www.24h.com.vn/xe-may-xe-dap-c748.html',
    'https://www.24h.com.vn/thi-truong-tieu-dung-c52.html',
    'https://www.24h.com.vn/du-lich-24h-c76.html',
    'https://www.24h.com.vn/suc-khoe-doi-song-c62.html',
    'https://www.24h.com.vn/cuoi-24h-c746.html',
    'https://www.24h.com.vn/media-24h-c762.html'
]

VN24H_XPATH = {
    'news_link': "//div[@id='left']//div[@class='postx']/article[contains(@class,'bxDoiSbIt')]/header//a/@href",
    'time': "//div[@id='left']/main//section/article[contains(@class,'nwsHt')]/div[contains(@class,'updTm updTmD')]/text()",
    'title': "//div[@id='left']/main//section/article[contains(@class,'nwsHt')]/header/h1/text()",
    'description': "//div[@id='left']/main//section/article[contains(@class,'nwsHt')]/h2[@class='ctTp']/text()",
    'content': "//div[@id='left']/main//section/article[contains(@class,'nwsHt')]/p/text()",
    'author': "//div[@id='left']/main//div[contains(@class,'nguontin')]//text()",
    'tag': "//div[contains(@class,'block_tag')]/h3/a/text()",
    'next_page': "//div[@id='left']/main//article[contains(@class,'pgCate')]//ul[@class='pg']/li[contains(@class, 'pgAt')]/a/@href"
}
