import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

ranks = soup.find('ol', {'id':'realTimeRankUpdate'}).find_all('li')		# 업데이트순
# ranks = soup.find('ol', {'id':'realTimeRankFavorite'}).find_all('li')	# 인기순

list_title = []
list_url = list()
for rank in ranks:
	list_title.append(rank.find("a")["title"])
	list_url.append('https://comic.naver.com' + rank.find("a")["href"])

df = pd.DataFrame({"title":list_title, "url":list_url})
df.to_excel("네이버웹툰_업데이트순.xlsx", index=False)