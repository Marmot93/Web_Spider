from bs4 import BeautifulSoup
import requests
import pymongo
import time

# 数据库
client = pymongo.MongoClient('localhost',27017)
wuba = client['wuba']
url_list = wuba['url_list']         # 列表页
item_info = wuba['ietm_info']       #详细信息


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
    price = soup.select('div.price_li > span')[0].text
    add = soup.select('div.palce_li > span > i')[0].text
    looked = soup.select('p > span.look_time')[0].text
    info = soup.find_all(attrs='baby_kuang clearfix')[0].text
    seller = soup.select('p.personal_name')[0].text

    item_info.insert_one({'title': title, 'price': price, 'add': add, 'info': info,
                              'seller': seller, 'looktimes': looked, 'link': url})
    # print({'title': title, 'price': price, 'add': add, 'info': info,
    #                           'seller': seller, 'looktimes': looked, 'link': url})
