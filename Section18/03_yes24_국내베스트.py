# 베스트도서 페이징 반복데이타가져오기

import requests
from bs4 import BeautifulSoup

list_title = list()
list_author = list()
for page in range(1, 4):
    # yes24 국내베스트
    url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06&fetchSize=40&PageNumber=" + str(page)

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("td", attrs={"class":"goodsTxtInfo"})                

    for item in items:
        title = item.find("p").find("a").get_text()                             # 책제목
        author = item.find("div", attrs={"class":"aupu"}).find("a").get_text()  # 저자

        list_title.append(title)
        list_author.append(author)


import pandas as pd
df = pd.DataFrame({"title":list_title, "author":list_author})
df.to_excel("yes24_국내베스트.xlsx", index=False)
