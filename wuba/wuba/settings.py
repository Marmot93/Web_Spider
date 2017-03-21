# -*- coding: utf-8 -*-

BOT_NAME = 'wuba'

SPIDER_MODULES = ['wuba.spiders']
NEWSPIDER_MODULE = 'wuba.spiders'


ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1 # 延迟

ITEM_PIPELINES = {
   'wuba.pipelines.WubaPipeline': 300,
}
# # 配置redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"    #调度
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #去重
# SCHEDULER_PERSIST = True       #不清理Redis队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"    #队列

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = "wuba"
MONGODB_DOCNAME = "zufang"

# REDIS_HOST = '192.168.1.199'
# REDIS_PORT = 6379
