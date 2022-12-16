import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows 한글폰트깨짐 해결
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac 한글폰트깨짐 해결
matplotlib.rcParams['font.size'] = 15                # 폰트 크기
matplotlib.rcParams['axes.unicode_minus'] = False    # 마이너스 글자 깨짐 해결

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
df = pd.DataFrame(data)
df.to_excel('school.xlsx')
plt.plot(df['이름'], df['키'])
# plt.show()
# plt.savefig('./Section19/school.png')                                 # 상대경로
plt.savefig('C:/dev/python/pythonstudy/workspace/Section19/school.png') # 절대경로