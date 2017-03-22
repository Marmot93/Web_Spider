import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import WubaItem
import re
import webbrowser


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
                item['huxing'] = i.xpath('div[2]/p[1]/text()').extract_first().split()
                # 直接抽不出来地址，就先提取再正则
                add = i.xpath('div[2]/p[2]').extract_first()
                item['add'] = re.findall('>(.*?)</a>',add)
                item['price'] = i.xpath('div[3]/div[2]/b/text()').extract_first()
                link = i.xpath('div[2]/h2/a[1]/@href').extract_first()
                item['link'] = link
            except Exception:
                print(response.url + ' 页的url抓取完成')
                pass
            yield scrapy.Request(link,meta={'item':item}, callback=self.parse_1)

            next_page = response.xpath('//a[@class="next"]/@href').extract_first()
            if next_page is not None:
                # next_page = response.urljoin(next_page) # 这里直接就给出了下一页的链接，不需要urljoin了
                yield scrapy.Request(next_page, callback=self.parse)

    def parse_1(self,response):
        item = response.meta['item']
        try:
            item['det'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[6]/span[2]/text()').extract_first().split()
            item['chaoxiang'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[3]/span[2]/text()').extract_first().split()
            item['xiaoqu'] = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[4]/span[2]/a/text()').extract_first().split()
            item['time'] = response.xpath('/html/body/div[4]/div[1]/p/text()').extract_first().split()
        except Exception:
            print('该页似乎消失了' + str(item['link']))
            webbrowser.open(str(item['link']),new=0,autoraise=True)

        yield item