import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.perekrestok.ru/cat/mc/1066/vse-dla-novogo-goda"

# Отправляем GET-запрос к странице
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML-страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим интересующие нас элементы на странице
    products = soup.find_all('div', class_='product-card__title')

    # Создаем список для хранения данных
    data = []

    # Выводим найденные названия продуктов и цены, записываем их в список
    for product in products:
        product_name = product.text.strip()
        product_price_container = product.find_next('div', class_='product-card__price')
        product_price = product_price_container.find('div', class_='price-new').text.strip().replace('\xa0', '') if product_price_container else "Цена не указана"
        print(f"Товар: {product_name}, Цена: {product_price}")
        data.append([product_name, product_price])

    # Создаем DataFrame из списка данных
    df = pd.DataFrame(data, columns=['Товар', 'Цена'])

    # Записываем DataFrame в CSV-файл
    df.to_csv('products.csv', encoding='utf-16', index=False, sep='\t')

    print("Данные успешно записаны в products.csv")
else:
    print(f"Ошибка при запросе: {response.status_code}")
