##### 리스트 메소드
# append()
my_list = ['apple', 'banana']
my_list.append('cherry')

# extend()
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango'])

# insert()
my_list = ['apple', 'banana']
my_list.insert(0, 'cherry')

# clear()
my_list = ['apple', 'banana']
my_list.clear()

# pop()
my_list = ['apple', 'banana']
my_list.pop()

# remove()
my_list = ['apple', 'banana']
my_list.remove('apple')

##### 세트 메소드
# 교집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
# s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# 합집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
# s3 = s1 | s2
s3 = s1.union(s2)
print(s3)

# 차집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
# s3 = s1 - s2
s3 = s1.difference(s2)
print(s3)
