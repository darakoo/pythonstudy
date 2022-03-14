'''
try:
    score = int(input('점수를 입력하세요 >>> '))

    # 점수가 음수이거나 100점 초과시 강제 예외 처리(메시지내용:점수는 0~100 사이입니다.)
except Exception as e:
    print(e)
else:
    # 80점 이상은 합격, 아닐경우 불합격을 출력하세요.
'''

########################################################
try:
    score = int(input('점수를 입력하세요 >>> '))
    if score < 0 or score > 100:
        raise Exception('점수는 0~100 사이입니다.')
except Exception as e:
    print(e)
else:
    if score >= 80:
        print('{}점은 합격입니다.'.format(score))
    else:
        print('{}점은 불합격입니다.'.format(score))
