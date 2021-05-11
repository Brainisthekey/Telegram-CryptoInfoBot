import bs4
import requests

def get_price_c(currency):
    price = requests.get(url=f'https://coinmarketcap.com/currencies/{currency}/').text
    soup = bs4.BeautifulSoup(price, 'html.parser')
    price = soup.find("div", {'class': 'priceValue___11gHJ'})
    return bs4.Tag.getText(price)
