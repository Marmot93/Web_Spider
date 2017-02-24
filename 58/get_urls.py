from multiprocessing import Pool
from  channel_extract import  channel_urls
from page_spider import get_links_from

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)


if __name__ == '__main__':
    pool = Pool()     #多进程（process = num）
    pool.map(get_all_links_from,channel_urls.split())  #map 把后面的依次放入前面的函数然后运行