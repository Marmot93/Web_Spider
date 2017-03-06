from bs4 import BeautifulSoup
import requests


headers = {'User_Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
           }
url = 'http://www.tripadvisor.cn/Search-a_confirm.true-a_confirmDist.false-a_searchSessionId.63E974677B6832FB44513168903C59491487777512728ssid-q%E6%88%90%E9%83%BD%E9%AB%98%E6%96%B0%E9%85%92%E5%BA%97?searchFilter=h&distance=&sort=r'
web_data = requests.get(url,headers=headers)
soup = BeautifulSoup(web_data.text,'lxml')

names = soup.select('div.info > div.title')
address = soup.select('div.address')
imgs = soup.select('img.photo_image')
prices = soup.select('price autoResize')



for name,addres,img,price  in zip(names,address,imgs,prices):
    data = {
        'name':name.get_text(),
        'add' : addres.get_text(),
        'img' : img.get('src'),
        'price' : prices.get_text()
    }
    print(data)
# 输出