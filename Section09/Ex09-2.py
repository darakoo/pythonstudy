##### 숫자 내장 함수
# abs() : 절대값
print(abs(10))
print(abs(-10))

# divmod() : 몫과 나머지를 한쌍의 튜플로 반환 
print('divmod()')
result = divmod(10000, 3000)
print(f'빵을 {result[0]}개 사고 {result[1]}원이 남았습니다.')
count, change = divmod(10000, 3000)    # 언패킹 : 리스트나 튜플의 요소를 여러 개의 변수에 나누어 담는 것이 가능
print(f'빵을 {count}개 사고 {change}원이 남았습니다.')

# float() : 전달된 인수를 float로 반환
# int() : 전달된 인수를 int로 반환

# max() : 전달된 인수 중 가장 큰 값을 반환
print('max()')
a = [2,99999]
b = [2,323,3523,2]
print(max(a, b))    # max 데이터가 있는 객체 return
print(max(1,4,6))

# min() : 전달된 인수 중 가장 작은 값을 반환
print(min(1,4,6))

# pow() : 거듭제곱(power) 반환
print(pow(10,2))              

# sum() : 반복가능객체(list, tuple)의 합계를 반환
print('sum()')
a = [1,2,3]
print(sum(a))

# round() : 반올림 반환
# 참고 http://mkseo.pe.kr/blog/?p=2688
# 끝자리 값이 5로 끝나는 경우에 한해서는 주의해서 사용할 필요가 있다.
# 파이썬은 round half even 방식으로 계산한다.
# round half even : 반올림 결과가 홀수이면 버림, 결과가 짝수이면 올림
print('round()')
print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(-0.5))
print(round(-1.5))
print(round(2.675, 2))

print('round()')
print(round(0.51))
print(round(1.51))
print(round(2.51))
print(round(3.51))

# round half up 방식으로 처리하고 싶을 경우는 0.5를 더해서 연산 한다.
print('round()')
print(round(0.5 + 0.5))
print(round(1.5 + 0.5))
print(round(2.5 + 0.5))
print(round(3.5 + 0.5))