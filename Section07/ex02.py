# for문과 list

# 리스트 안에서 for 사용하기
list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list = [num*2 for num in list]
print(list)

# 리스트 안에서 for, if 사용하기
list = [ num * 3 for num in list if num % 2 == 0 ]
print(list)
