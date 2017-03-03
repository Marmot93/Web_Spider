import requests
from lxml import etree

# 用xpath重构58详细信息抓取spider
def spider_item_info(url):

    html = requests.get(url).text
    selector = etree.HTML(html)

    title = selector.xpath('/html/head/title/text()')[0].strip()
    price = selector.xpath('//span[@class="price_now"]/i/text()')[0]
    add = selector.xpath('//div[@class="palce_li"]/span/i/text()')[0]
    info = selector.xpath('//div[@class="baby_kuang clearfix"]/p/text()')[0]
    data = {
        'title':title,
        'price':price,
        'add':add,
        'info':info,
    }
    print(data)

# 只做测试，用多进程map函数对 sipder_item_info()导入所有url即可
url = 'http://zhuanzhuan.58.com/detail/837482115974103043z.shtml'
spider_item_info(url)