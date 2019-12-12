'''
Use the BeautifulSoup and requests Python packages
to print out a list of all the article titles on the New York Times homepage.
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
articles = soup.find_all('article')
article_titles = [article.h2.string for article in articles]

for title in article_titles:
	print(title)