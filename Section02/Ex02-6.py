#=====컬렉션:set

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

a = {1,2,3,4}   
b = {1,2,3,5}  
print(type(a))
print(dir(a))

a.add(1)    # 추가 안됨
a.add(5)    # 추가 됨
print(a)

print(a.difference(b))
print(a)
a.difference_update(b)
print('difference_update:', a)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1 & s2
s1.intersection(s2)

s1 | s2
s1.union(s2)

s1 - s2
s1.difference(s2)