'''
[파일명:pr03-3]
[문제]
딕셔너리를 이용하여 영어사전을 구현합니다.
[실행예]
영어 단어를 입력하세요 >>> fly
fly: 날다
[힌트]
english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
'''

english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
word = input('영어 단어를 입력하세요 >>> ')
print('{}: {}'.format(word, english_dict.get(word)))
print('{}: {}'.format(word, english_dict[word]))
