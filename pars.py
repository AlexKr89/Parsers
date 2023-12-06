import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.perekrestok.ru/cat/d"

# Отправляем GET-запрос к странице
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML-страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим интересующие нас элементы на странице
    products = soup.find_all('div', class_='product-card__title')

    # Создаем CSV-файл для записи данных
    with open('products.csv', mode='w', encoding='utf-16', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Товар', 'Цена'])

        # Выводим найденные названия продуктов и цены, записываем их в CSV
        for product in products:
            product_name = product.text.strip()
            product_price_container = product.find_next('div', class_='product-card__price')
            product_price = product_price_container.find('div', class_='price-new').text.strip() if product_price_container else "Цена не указана"
            print(f"Товар: {product_name}, Цена: {product_price}")
            writer.writerow([product_name, product_price])

    print("Данные успешно записаны в products.csv")
else:
    print(f"Ошибка при запросе: {response.status_code}")
