#=====컬렉션:list

# 컬렉션 종류
a = [1,2,3]                     # list
a = (1,2,3)                     # tuple
a = {1,2,3}                     # set
a = {'age':25, 'name':'Alice'}  # dict

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
a = [100, 3.14, 'hello']
print(dir(a))
print(a[0])
a = [1, 2, 3, 4]
a.append(5)
print(a)
print(a.count(3))
a.extend([6,7,8])
print(a)
a.insert(0, 0)
print(a)
print(a.pop())
print(a)
a.pop(0)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.remove(5)
print(a)

'''
#=====컬렉션:tuple
a = 1,
a = 1,2,3
a = (1,2,3)

#=====컬렉션:set
a = {1,2,3,4,5}
a.add(2) # 추가안됨
a.add(6) # 추가됨
a.remove(1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1 & s2
s1.intersection(s2)

s1 | s2
s1.union(s2)

s1 - s2
s1.difference(s2)

#=====컬렉션:dic
dic = {'name':'Tom', 'phone':'01022223333', 'birth': '1118'}
dic.update(name = 'Sam')
print(dic.get('name'))
print(dic)
print(dic.items())
print(dic.keys())

#=====mutable과 immutable
#교재참고

'''