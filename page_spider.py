from bs4 import BeautifulSoup
import requests
import pymongo
import time

client = pymongo.MongoClient('localhost',27017)
wuba = client['wuba']
url_list = wuba['url_list']


# spider 1 抓取列表页
def get_links_from(chinnel_urls,pages,who_sell=0):
    # http: // cd.58.com / iphonesj / pn3 /
    # 列表页构成
    list_pages = '{}{}/pn{}' . format(chinnel_urls,str(who_sell),str(pages))
    web_data = requests.get(list_pages)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text,'lxml')       #解析列表页

    if soup.find('td','t'):                         # 找不到td.t就跳过
        for link in soup.select('td.t a.t'):            #抽取详情页
            if 'zhuanzhuan.58'  in str(link):           #干掉智能58精准搜索
                item_link = link.get('href').split('?')[0]
                url_list.insert_one({'url':item_link})
    else:
        pass

# spide 2 抓取商品信息
def get_item_info(url):
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text,'lxml')

    title = str(soup.title.text.split('_')[0]).split('】')[1]
    price = soup.select('price_now')
    add = soup.select('palce_li')
    info = soup.select('icon_png sanjiao')


    print(title)
get_item_info('http://zhuanzhuan.58.com/detail/834682811900149763z.shtml')