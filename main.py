import requests
from bs4 import BeautifulSoup


URL = 'https://statusinvest.com.br/fundos-imobiliarios/'

class StockData:
    def __init__(self, stock):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }

        self.page = requests.get(URL+stock, headers=self.headers)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.dividents = self.soup.find('input', {'id': 'results'}).get('value')
        print(self.dividents)

StockData('BCFF11')