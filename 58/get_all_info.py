from multiprocessing import Pool
from page_spider import get_item_info
import pymongo

client = pymongo.MongoClient('localhost',27017)
wuba = client['wuba']
url_list = wuba['url_list']
item_info = wuba['ietm_info']


list = []
for url in url_list.find():
    list.append(url['url'])

if __name__ == '__main__':
    pool = Pool()     #多进程（process = num）
    pool.map(get_item_info,list)