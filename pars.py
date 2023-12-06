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
    with open('products.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Товар'])

        # Выводим найденные названия продуктов и записываем их в CSV
        for product in products:
            product_name = product.text.strip()
            print(f"Товар: {product_name}")
            writer.writerow([product_name])

    print("Данные успешно записаны в products.csv")
else:
    print(f"Ошибка при запросе: {response.status_code}")
