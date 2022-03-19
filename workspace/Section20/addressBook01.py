# [문제]
# 주소록을 관리하는 프로그램입니다. 아래 지시사항을 구현하세요.
# 1. 등록 로직 구현하기
# 2. 검색 로직 구현하기
# 3. phone 을 tel 로 변경하기
# 4. email 정보 추가하기
# 5. 주소록 파일명을 클래스 변수로 처리하기 file_name ='./Section20/addressBook01.csv'
#    - self.file_name 으로 읽으면 된다.

import sys

class Person:

    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))


class AddressBook:

    def __init__(self):
        self.address_list = []
        self.file_reader()
        print(self.address_list)

    def menu():
        print('-' * 30)
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('프로그램 종료는 0번')
        print('-' * 30)
        choice = int(input('수행할 작업을 숫자로 입력하세요 >>> '))
        return choice

    def run(self):
        while True:
            choice = AddressBook.menu()
            if choice == 0: self.exit()
            elif choice == 1: self.insert()
            elif choice == 2: self.delete()
            elif choice == 3: self.update()
            elif choice == 4: self.search()
            elif choice == 5: self.printAll()
            else: print('없는 명령입니다. 확인 후 다시 입력하세요.')
    
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()

    def file_reader(self):
        try:
            file = open('addressBook.csv', 'rt')  # 파일이 없으면 예외 발생
        except:  # 예외 처리 (파일이 없을 때)
            print('addressBook.csv 파일이 없습니다.')
        else:  # 정상 처리 (파일이 있을 때)
            while True:
                buffer = file.readline()
                if not buffer:
                    break
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                addr = buffer.split(',')[2].rstrip('\n')
                self.address_list.append(Person(name, phone, addr))
            print('addressBook.csv 파일을 로드했습니다.')
            file.close()

    def file_generator(self):
        try:
            file = open('addressBook.csv', 'wt')  
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write('{},{},{}\n'.format(person.name, person.phone, person.addr))
            file.close()

    def insert(self):
        print('=== 신규 주소록 생성 ===')
        # 구현하세요.

    def delete(self):
        print('=== 기존 주소록 삭제 ===')
        name = input('삭제할 이름 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 삭제를 취소합니다.')
            return
        deleted = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다.'.format(self.address_list[i].phone))
                if input('삭제할까요?(Y/N) >>> ').upper() != 'Y':
                    continue  # for문으로 되돌아가서 다음 사람을 검색
                self.address_list.pop(i)  # 삭제
                deleted = True
                print('{}의 정보를 삭제했습니다.'.format(name))
                self.file_generator()
                break
        if not deleted:
            print('{}의 정보가 삭제되지 않았습니다.'.format(name))

    def update(self):
        print('=== 기존 주소록 수정 ===')
        name = input('수정할 이름 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 수정을 취소합니다.')
            return
        updated = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다.'.format(self.address_list[i].phone))
                if input('수정할까요?(Y/N) >>> ').upper() != 'Y':
                    continue  # for문으로 되돌아가서 다음 사람을 검색
                new_phone = input('변경할 전화번호 입력 >>> ')
                if new_phone:  # 입력이 있으면
                     self.address_list[i].phone = new_phone  # 입력된 내용으로 변경
                new_addr = input('변경할 주소 입력 >>> ')
                if new_addr:
                    self.address_list[i].addr = new_addr
                updated = True
                print('주소록이 수정되었습니다. 수정된 주소록의 내용을 확인하세요.')
                self.address_list[i].info()
                self.file_generator()
                break
        if not updated:
            print('{}의 정보가 수정되지 않았습니다.'.format(name))

    def printAll(self):
        print('=== 전체 연락처 출력 ===')
        for person in self.address_list:
            person.info()
        print('총 {}개의 주소록이 있습니다.'.format(len(self.address_list)))

    def search(self):
        print('=== 주소록 검색 ===')
        # 구현하세요.

# ↑ class AddressBook 종료 ↑


my_app = AddressBook()  # my_app 인스턴스 생성
my_app.run()  # my_app 실행
my_app.printAll()
