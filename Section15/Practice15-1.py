'''
[문제]
다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book클래스를 생성하세요.
[실행예]
책 제목: Python
책 저자: 김파이
책 제목: java basic
책 저자: 김자바
[지시사항]
1. 책제목과 책저자 정보를 출력하는 print_info() 메소드를 구현하고 인스턴스를 생성하세요.
2. class Book 정보는 아래와 같습니다.
 class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author
'''

class Book:

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print('책 제목: {}'.format(self.title))
        print('책 저자: {}'.format(self.author))


# book1, book2 인스턴스의 생성
book1 = Book()
book2 = Book()

# book1, book2 제목과 저자 정보 저장
book1.set_info('파이썬', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')

book1.print_info()
book2.print_info()

# 아래와 같이 출력도 가능하다.
book_list = [book1, book2]
for book in book_list:
    book.print_info()
