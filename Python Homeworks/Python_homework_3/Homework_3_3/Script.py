import requests
from bs4 import BeautifulSoup
url = "https://example.com"

response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h2')
    for article in articles:
        print(article.text)
else:
    print(f"Ошибка при запросе: {response.status_code}")