'''
n = 1
while n <= 100:
    if(n % 10 == 0):
        print(n, end='\n')
    else:
        print(n, end='\t')
    n += 1

'''
n = 1
while n<=10:
    print(n, end='\t')
    n += 1
a = (1,2,3)
for n in a:
    print(n, end=' ')
a = [1,2,3]
for n in a:
    print(n, end=' ')
b = (1,2,3)
a = [n*2 for n in b]
print(a)

print(range(1,6))

for n in range(11):
    print(n, end='')

for n in [1,2,3,4,5,6,7,8,9,10]:
    print(n, end='')

