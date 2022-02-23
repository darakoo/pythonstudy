from datetime import *

start = datetime.datetime.now()
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.datetime.now()

elapse = end - start
elapse = elapse.total_seconds()

print('총 합은 {}입니다.'.format(total))
print('총 {}초가 소요되었습니다.'.format(elapse))
