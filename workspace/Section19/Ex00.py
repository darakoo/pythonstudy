#========== 목차 정리와 전체 내용 설명하기

#========== matplotlib
#===== matplotlib 설치하기
# 명령 프롬프트에서 설치 : pip install matplotlib

'''
#===== figure, subplot : 그래프 그리기
# figure : subplot을 포함하는 전체 영역
# subplot : 그래프를 그리는 영역
import matplotlib.pyplot as plt

figure = plt.figure()
# 1행 1열 1번째 subplot
axes = figure.add_subplot(1, 1, 1)
# 아래 부분을 주석 해제 후 실행 하면 매개변수를 이해할 수 있다.
# axes = figure.add_subplot(2, 2, 4)
plt.show()

#===== plot() : 꺽은선 그래프 그리기1
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = [0, 1, 2, 3, 4]
y = [4, 1, 3, 5, 2]
axes.plot(x, y)
plt.show()

#===== plot() : 꺽은선 그래프 그리기2
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x1 = [0, 1, 2, 3, 4]
y1 = [4, 1, 3, 5, 2]
x2 = [0, 1, 2, 3, 4]
y2 = [0, 8, 5, 3, 1]
axes.plot(x1, y1)
axes.plot(x2, y2)
plt.show()

#===== plot() : 꺽은선 그래프 그리기3
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x1 = [0, 1, 2, 3, 4]
y1 = [4, 1, 3, 5, 2]
x2 = [0, 1, 2, 3, 4]
y2 = [0, 8, 5, 3, 1]
axes.plot(x1, y1, linestyle='dotted', linewidth=5.0)
axes.plot(x2, y2, color='r', marker='v')
plt.show()

#===== 한글처리 skip

#===== 기본예제 01

#===== bar() : 막대 그래프
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = [0, 1, 2, 3, 4]
y = [4, 1, 3, 5, 2]
axes.bar(x, y)
plt.title('title')
plt.xlabel('x name')
plt.ylabel('y name')
plt.show()

#===== scatter() : 산포 그래프
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = [0, 1, 2, 3, 4]
y = [4, 1, 3, 5, 2]
area = [50, 100, 150, 200, 250] # 점의 크기
color = ['red', 'green', 'blue', 'orange', 'aqua'] # 점의 색상
axes.scatter(x, y, s = area, c = color)
plt.show()

#===== 기본예제 02 실행하기


#===== pie() : 원형 그래프1
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
data = [1, 2, 3]
axes.pie(data)
plt.axis('equal') # 일반원
plt.show()

#===== pie() : 원형 그래프2
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
data = [1, 2, 3]
label = ['good', 'bad', 'normal']
axes.pie(data, labels = label, autopct = '%d%%') # %d:정수표시, %%:두개사용한 이유는 %가 이스케이프문자
plt.axis('equal') # 일반 원
plt.show()

#===== wordcloud() : 문자 그래프
# pip install wordcloud  설치하기
# 소스 전달 후 분석

import matplotlib.pyplot as plt
import wordcloud

words = {
    '파이썬':30,
    'java':3,
    'C':7,
    'html':9,
    'jsp':12,
}
wc = wordcloud.WordCloud()
# wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/HMFMPYUN.TTF')
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()
'''

#===== 응용예제 : 소스 전달 후 풀이

