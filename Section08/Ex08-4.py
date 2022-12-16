'''
[문제]
사용자로부터 5개의 양의 정수를 입력받아 그 합계를 구하세요.
'''

count = 1
total = 0
while count < 6:
    n = int(input('{}번째 정수를 입력하세요 >>> '.format(count)))
    if n <= 0:
        print('0 이하의 정수는 처리할 수 없습니다.')
        continue
    total += n
    count += 1
print('입력된 5개 양수의 총 합은 {}입니다.'.format(total))
