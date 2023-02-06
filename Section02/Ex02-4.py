# 컬렉션 자료형 : list, tuple, set, dict
a = [1,2,3]                     # list
a = (1,2,3)                     # tuple
a = {1,2,3}                     # set
a = {'age':25, 'name':'Alice'}  # dict

# list
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
a = [100, 3.14, 'hello']
print(dir(a))
print(a[0])
a = [1, 2, 3, 4]
a.append(5)
print(a.count(3))
a.extend([6,7,8])
a.insert(0, 0)
print(a.pop())
a.pop(0)
a.reverse()
a.sort()
a.remove(5)