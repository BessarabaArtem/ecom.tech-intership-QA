import requests

# 1. Проверка доступности главной страницы
url = "https://kuper.ru"
response = requests.get(url)

if response.status_code == 200:
    print("Главная страница работает, код 200")
else:
    print("Ошибка, код:", response.status_code)

# 2. Проверка текста на главной
if "Купер - быстрый сервис доставки" in response.text:
    print("Текст найден")
else:
    print("Текст НЕ найден")

# 3. Получить список городов
# Взял хедеры из браузера чтобы работало, иначе 403 ошибка :(
api_url = "https://kuper.ru/api/v2/regions" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

try:
    res = requests.get(api_url, headers=headers)
    if res.status_code == 200:
        print("Список городов получен")
    else:
        print("Не удалось получить города, код:", res.status_code)
except:
    print("Что-то пошло не так с запросом")