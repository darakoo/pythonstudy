#=====컬렉션:dict
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
a = {'name':'Tom', 'phone':'01022223333', 'birth': '1118'}
print(type(a))
print(dir(a))
print('fromkeys')
x = ('names', 'phone')
print(a.fromkeys(x))
a.update(name = 'Sam')
print(a.get('name'))
print(a.items())
print(a.keys())
print(a.pop('name'))
print(a)
print(a.popitem())
print(a)
print(a.values())