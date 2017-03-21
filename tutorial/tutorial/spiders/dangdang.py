import scrapy

class DangSpider(scrapy.Spider):
    name = 'tushu'
    start_urls = ['http://category.dangdang.com/cp01.00.00.00.00.00.html']
    # 三层分类
    def parse(self, response):
        lab_big = response.css('a.t::attr(href)')
        lab_big_page = response.urljoin(lab_big)
        yield scrapy.Request(lab_big_page, callback=self.parse_lab_big)

    def parse_lab_big(self, response):
        lab_mid = response.xpath('//*[@id="leftCate"]/ul/li/a/@href')
        lab_mid_page = response.urljoin(lab_mid)
        yield scrapy.Request(lab_mid_page, callback=self.parse_lab_mid)

    def parse_lab_mid(self, response):
        lab_lit = response.xpath('//*[@name="C1"]/span/a/@href')
        lab_lit_page = response.urljoin(lab_lit)
        yield scrapy.Request(lab_lit_page, callback=self.parse_info)

    def parse_info(self, response):
        for shu in response.css('div.inner'):
            yield {
            'name': shu.css('p.name a::text ').extract_first(),
            'commen': shu.css('p.star a::text').extract_first().replace('条评论', '') ,
            'time': shu.css('p.publishing_time::text').extract_first().replace('/', '').strip(),
            'press': shu.css('p.publishing a::text').extract_first().replace('/', '').strip(),
            'price': shu.css('p.price span.price_n::text').extract_first().replace('¥', ''),
            'lable_big': response.css('div.sort_box h3::text').extract_first(),
            }


