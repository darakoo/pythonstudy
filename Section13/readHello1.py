file = open('hello.txt', 'rt')

str = file.read()
print(str, end='')
# print(str)

file.close()
