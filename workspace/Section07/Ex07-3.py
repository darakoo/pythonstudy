# for문과 dict
# 다음은 영어 사전을 딕셔너리 자료형으로 구현하고 영어 사전에 등록된 모든 단어와 그 단어의 의미를 출력하는 프로그램입니다.

eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
    }
for word in eng_dict:
    print('{}의 뜻: {}'.format(word, eng_dict.get(word)))
