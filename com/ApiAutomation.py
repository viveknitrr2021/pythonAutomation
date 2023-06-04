import requests

r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-5-27&to=2023-5-28&sortBy=popularity&language=en&apiKey=f9666141dbf541619fddd4452b04d110")
content = r.json()

print(content['articles'][0]['title'])