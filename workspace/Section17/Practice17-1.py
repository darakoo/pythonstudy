# [문제]
# 우리나라의 도를 맞히는 Quiz 클래스를 구현하세요.
# [실행 예]
# 우리나라의 도를 맞히는 퀴즈입니다.
# 정답은? >>> 경기도
# 정답 입니다.
# 정답은? >>> 울릉도
# 틀렸습니다.

class Quiz:

    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']  # 한 줄로 작성

    @classmethod
    def challenge(cls):
        do = input('정답은? >>> ')
        # 정답 일때 : 
        # 오답 일때 : Exception을 강제로 발생 시킨다.
        # ???

try:
    print('우리나라의 도를 맞히는 퀴즈입니다.')
    # challenge() 호출
    # ???

except Exception as e:
    print(e)



'''
class Quiz:

    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']  # 한 줄로 작성

    @classmethod
    def challenge(cls):
        do = input('정답은? >>> ')
        if do in cls.answer:
            print('정답 입니다.')
        else:
            raise Exception('틀렸습니다.')

        # cls.challenge()

try:
    print('우리나라의 도를 맞히는 퀴즈입니다.')
    while True:
        Quiz.challenge()
except Exception as e:
    print(e)


class Quiz:

    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도', '전라북도', '경상남도', '경상북도', '제주특별자치도']  # 한 줄로 작성

    @classmethod
    def challenge(cls):
        if not cls.answer:
            print('모든 도를 맞혔습니다. 성공입니다.')
            return
        do = input('정답은? >>> ')
        if do not in cls.answer:
            raise Exception('틀렸습니다.')
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do:
                print('정답입니다.')
                cls.answer.pop(i)
                break
        cls.challenge()
'''