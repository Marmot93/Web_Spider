import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import WubaItem
import re


class WuSpider(scrapy.Spider):
    name = 'zufang'
    start_urls = ['http://cd.58.com/chuzu/0/pn1/']
    redis_key = 'zufang:start_urls'
    allowed_domains = ["58.com"]

    def parse(self, response):
        for i in response.xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li'):
            item = WubaItem()
            try:
                item['title'] = i.xpath('div[@class="des"]/h2/a[1]/text()').extract_first().split('|')[1]
                item['huxing'] = i.xpath('div[2]/p[1]/text()').extract_first()
                # 直接抽不出来地址，就先提取再正则
                add = i.xpath('div[2]/p[2]').extract_first()
                item['add'] = re.findall('>(.*?)</a>',add)
                item['price'] = i.xpath('div[3]/div[2]/b/text()').extract_first()
            except Exception:
                print('翻页')
                pass
            yield item

            next_page = response.xpath('//a[@class="next"]/@href').extract_first()
            if next_page is not None:
                # next_page = response.urljoin(next_page) # 这里直接就给出了下一页的链接，不需要urljoin了
                yield scrapy.Request(next_page, callback=self.parse)

