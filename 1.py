from bs4 import BeautifulSoup
import requests

url = 'http://www.tripadvisor.cn/'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')

countrys = soup.select('div.title > a.countryName ')
citys = soup.select('div.title > a.cityName')
imgs = soup.select('a > span.thumbCrop > img')


for country,city,img in zip(countrys,citys,imgs):
    data = {
        'country':country.get_text(),
        'city': city.get_text(),
        'img': img.get('src')
    }
    print(data)