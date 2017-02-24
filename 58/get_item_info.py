from multiprocessing import Pool
from page_spider import get_item_info
import pymongo

client = pymongo.MongoClient('localhost',27017)
wuba = client['wuba']
url_list = wuba['url_list']
item_info = wuba['ietm_info']

for url in url_list.find() :
    get_item_info(url['url'])