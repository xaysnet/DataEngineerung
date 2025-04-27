import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import datetime
import json
import os

# Имитация браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Основная структура где будет хранится инф.
class Company:
    def __init__(self, name, ticker, price_rub, PE, year_stonks, year_result_percent):
        self.name = name  # Название компании
        self.ticker = ticker  # Тикет компании
        self.price_rub = price_rub  # Цена акций в рублях
        self.PE = PE  # Коэффициент 
        self.year_stonks = year_stonks  # Акции
        self.year_result_percent = year_result_percent  # Процент прибыли за год
print("1")    

# Функция для получения текущего курса доллара
def get_usd_rate():
    formatted_date = datetime.datetime.now().strftime('%d/%m/%Y')
    cb_response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={formatted_date}')
    cb_xml = ET.fromstring(cb_response.text)
    return float(cb_xml.find(".//Valute[CharCode='USD']/Value").text.replace(',', '.'))
    
# Функция для сбора данных о компаниях
def scrape_companies(usd_rate):
    companies = []
    for i in range(2): # Перебераем страницы
        url = f'https://markets.businessinsider.com/index/components/s&p_500?p={i + 1}'
        stonks_request = requests.get(url, headers=headers)
        stonks_soup = BeautifulSoup(stonks_request.text, 'html.parser')
        companies_table = stonks_soup.find('tbody', class_='table__tbody')

        if companies_table: # Проверяем, была ли найдена компании
            for tr in companies_table.find_all('tr'):
                tds = tr.find_all('td')                    
                a_tag = tds[0].find('a')
                name = a_tag.get('title')
                # Операции с валютой
                USD_price_str = tds[1].get_text(strip=True, separator=' ').split()[0].replace(',', '')
                USD_price = float(USD_price_str)
                RUB_price = round(USD_price * usd_rate, 2)

                companies.append(Company(name, a_tag.get('href').split('/')[-1].split('=')[-1], RUB_price, None, None, None))
    return companies


usd_rate = get_usd_rate()
companies = scrape_companies(usd_rate)

# Сохраняем в папку "1" на диске "С"
output_dir = "C:\\1"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "rprice.json"), 'w', encoding='utf-8') as f:
    json.dump(create_json(top_price, "price"), f, indent=2)

with open(os.path.join(output_dir, "pe.json"), 'w', encoding='utf-8') as f:
    json.dump(create_json(top_pe, "P/E"), f, indent=2)

with open(os.path.join(output_dir, "growth.json"), 'w', encoding='utf-8') as f:
    json.dump(create_json(top_growth, "growth"), f, indent=2)

with open(os.path.join(output_dir, "potential.json"), 'w', encoding='utf-8') as f:
    json.dump(create_json(top_profit, "potential profit"), f, indent=2)
    
print("2")
