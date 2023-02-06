# yes24 책소개

# 1. 외부모듈 import
import requests
from bs4 import BeautifulSoup
import pandas as pd

# get user agent string 검색
# headers = {"Ueser-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

# 2. html 소스 추출
url = "http://www.yes24.com/Product/Goods/115142458"
# res = requests.get(url, headers=headers)
res = requests.get(url)
res.raise_for_status()

# 3. BeautifulSoup 객체 생성
soup = BeautifulSoup(res.text, "lxml")

# 4. 데이터 분석
contents = soup.find("textarea", attrs={"class":"txtContentText"}).get_text().strip() # 책소개
print(contents)              

# 5. 데이터 저장
with open('책소개.txt', 'wt') as file:
    file.write(contents)