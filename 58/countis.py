import time
from page_spider import url_list
from page_spider import item_info

while True:
    print(url_list.find().count())
    print(item_info.find().count())
    time.sleep(5)