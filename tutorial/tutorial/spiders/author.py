import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author + a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_author(self, response):
        def eatract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name':eatract_with_css('h3.author-title::text'),
            'born':eatract_with_css('span.author-born-date::text'),
            'description':eatract_with_css('div.author-description::text'),
        }