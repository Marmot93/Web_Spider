from multiprocessing import Pool
from page_spider import get_item_info
import pymongo

client = pymongo.MongoClient('localhost',27017)
wuba = client['wuba']
url_list = wuba['url_list']
item_info = wuba['ietm_info']


finded_url = [item['link'] for item in item_info.find()]
all_url = [item['url'] for item in url_list.find()]

lest_url = set(all_url) - set(finded_url)


if __name__ == '__main__':
    pool = Pool()     #多进程（process = num）
    pool.map(get_item_info,lest_url)
    pool.close()
    pool.join()