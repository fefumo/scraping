import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
def get_url():
    for count in range(1,8):
        url = f'https://scrapingclub.com/exercise/list_basic/?=page={count}'
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_='w-full rounded border')
        
        for str in data:
            card_url = 'https://scrapingclub.com' + str.find("a").get("href")
            yield card_url

for card_url in get_url():
    response = requests.get(card_url, headers = headers)
    sleep(3)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_='my-8 w-full rounded border')
    name = data.find("h3", class_='card-title').text
    price = data.find('h4', class_='my-4 card-price').text
    text = data.find('p', class_='card-description').text
    url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
    
    print(name + '\n' + price + '\n'+ text + '\n' + url_img, '\n')