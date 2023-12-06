import requests
from bs4 import BeautifulSoup
import pandas as pd

url = input("Введите ссылку для сбора данных: ")

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_='product-card__title')

    data = []

    for product in products:
        product_name = product.text.strip()
        product_price_container = product.find_next('div', class_='product-card__price')
        product_price = product_price_container.find('div', class_='price-new').text.strip().replace('\xa0', '') if product_price_container else "Цена не указана"
        print(f"Товар: {product_name}, Цена: {product_price}")
        data.append([product_name, product_price])

    df = pd.DataFrame(data, columns=['Товар', 'Цена'])

    df.to_csv('products.csv', encoding='utf-16', index=False, sep='\t')

    print("Данные успешно записаны в products.csv")
else:
    print(f"Ошибка при запросе: {response.status_code}")
