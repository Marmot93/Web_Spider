# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from .items import WubaItem

class WubaPipeline(object):
    def __init__(self):
        # 引用setting设置
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        db_doc = settings['MONGODB_DOCNAME']
        # 连接 MongoDB
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[db_name]
        self.post = tdb[db_doc]

    def process_item(self, item, spider):
        '''先判断itme类型，在放入相应数据库'''
        if isinstance(item,WubaItem):
            try:
                if item['price'] != None:
                    book_info = dict(item)
                    self.post.insert(book_info)
                    # if self.post.insert(book_info):
                        # print('插入')
            except Exception:
                pass
        return item
