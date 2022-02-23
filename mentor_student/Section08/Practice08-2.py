# [문제]
# 영화 평점을 1부터 5사이의 정수로 입력받아서 해당 평점만큼 '★'을 표시하는 프로그램을 구현하세요.
# 표시할 수 있는 평점의 범의를 벗어나면 재입력을 요구하세요.
# [실행예]
# 이번 영화의 평점을 입력하세요 >>> 10
# 평점은 1~5 사이만 입력할 수 있습니다.
# 이번 영화의 평점을 입력하세요 >>> -2 
# 평점은 1~5 사이만 입력할 수 있습니다.
# 이번 영화의 평점을 입력하세요 >>> 5  
# 평점: ★★★★★
# [힌트]

while True:
    grade = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if grade >= 1 and grade <= 5:
        print('평점: {}'.format('★' * grade))
        break
    else:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
