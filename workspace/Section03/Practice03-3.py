# [실행예]
# 영어 단어를 입력하세요 >>> fly
# fly: 날다
# [변수]
# english_dict, word

english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
word = input('영어 단어를 입력하세요 >>> ')
print('{}: {}'.format(word, english_dict[word]))
