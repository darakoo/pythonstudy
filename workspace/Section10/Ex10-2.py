a_list = ['above', 'cookie', 'app', 'about', 'admin', 'bisket', 'apple', 'april']
for i, item in enumerate(a_list):
    # print('idx : {}'.format(item.find('a')))
    if item.find('a') == 0:
        print('{} 제거됩니다.'.format(a_list.pop(i)))

print(a_list)
