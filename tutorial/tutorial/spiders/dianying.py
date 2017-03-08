import scrapy


class DySpider(scrapy.Spider):
    name = 'dy'
    start_urls = ['https://movie.douban.com/top250',]

    def parse(self, response):
        for move in response.css('div.info'):
            yield {
            'name':move.css('span.title::text').extract(),
            'mark':move.css('span.rating_num::text').extract(),
            'quote':move.css('span.inq::text').extract(),
            'info':move.css('div.bd p::text').extract(),
            }
        next_page = response.css('span.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)