# 반복 데이타
# yes24 메인 / 우측 상단 베스트 1위 ~ 10위

import requests
from bs4 import BeautifulSoup

url = "http://www.yes24.com"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("span", attrs={"class":"rnk_info"})                

# 전체 출력
for item in items:
    print(item.find("strong").get_text())                            # 책제목

# 1위~5위까지 출력
# for n in range(len(items)):
#     if n == 5:
#         break
#     print(items[n].find("strong").get_text())