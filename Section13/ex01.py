#===== 텍스트 파일 쓰기

# 파일명만 지정할 경우는 열기한 폴더가 root가 된다.
# 파일명 생성시 \'를 사용할 경우 \\'으로 처리해야 한다.
file = open('C:/dev/python/pythonstudy/workspace/Section13/hello.txt', 'wt', encoding='utf-8')
file = open('./Section13/hello.txt', 'wt', encoding='utf-8')
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
file.close()

# 텍스트 파일에 내용 추가하기
file = open('./Section13/hello.txt', 'at', encoding='utf-8')
file.write('내용을 추가합니다.')
file.write('\n')
file.close()