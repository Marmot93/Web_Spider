import requests
from lxml import etree
from multiprocessing import Pool

# s练习

url_list = ['http://tieba.baidu.com/p/3522395718?pn={}'.format(i) for i in range(1,797)]


def get_info(url):

    web_data = requests.get(url).text
    selector = etree.HTML(web_data)

    users = set(selector.xpath('//ul[@class="p_author"]/li[3]/a/text()'))
    info = selector.xpath('//*[@class="post_bubble_middle"]/text()')
    print(users)
    print(info)



if __name__ == '__main__':
    pool = Pool()
    pool.map(get_info,url_list)
    pool.close()
    pool.join()