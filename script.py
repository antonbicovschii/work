import requests
import dataframe_image
import pandas # Импортируем "инструмент" для запросов

# 1. Адрес (Endpoint), куда мы стучимся
url = "https://jsonplaceholder.typicode.com/users/3"

# 2. Отправляем GET-запрос (просим данные)
response = requests.get(url)

# 3. Проверяем статус-код (200 - это успех)
if response.status_code == 200:
    # 4. Превращаем "сырой" ответ в удобный формат JSON (словарь Python)
    data = response.json()

    print(f"Успех! Мы нашли пользователя.")
    print(f"Имя: {data['name']}")
    print(f"Email: {data['email']}")
    print(f"Город: {data['address']['city']}")
else:
    print(f"Ой, что-то пошло не так. Код ошибки: {response.status_code}")