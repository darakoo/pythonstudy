# 문제를 변형했음

# [문제]
# 조회, 입금, 출금 기능이 있는 BankAccount 클래스와 BankError 예외 클래스를 구현하세요.

# [실행 예]
# ===이체전===
# 계좌번호: 012-34-56789
# 통장잔액: 50000원
# 계좌번호: 987-65-43210
# 통장잔액: 50000원
# ===이체후===
# 계좌번호: 012-34-56789
# 통장잔액: 45000원
# 계좌번호: 987-65-43210
# 통장잔액: 55000원

# class BankError(Exception):
# 1. BankError 사용자 예외 클래스 구현

# class BankAccount:
# 2. 생성자 구현
# 인스턴스변수
# 계좌번호 : acc_no
# 통장 잔액 : balance

# 3. 입금 기능
# 메소드명 : deposit
# 매개변수 : money(입금할 금액)
# 반환값 : 없음
# 예외 상황 : 0원 이하 입금시

# 4. 출금 기능
# 메소드명 : withdraw
# 매개변수 : money(출금할 금액)
# 반환값 : 없음
# 예외 상황 : 0원 이하 출금 시, 통장 잔액보다 큰 금액 출금 시 

# 4. 조회 기능
# 메소드명 : inquiry
# 매개변수 : 없음
# 반환값 : 없음
# 기능 : 계좌번호, 잔액을 터미널에 출력


me = BankAccount('012-34-56789', 50000)
you = BankAccount('987-65-43210', 50000)

try:
    print('===이체전===')
    me.inquiry()
    you.inquiry()
    me.withdraw(5000)
    you.deposit(5000)
    print('===이체후===')
    me.inquiry()
    you.inquiry()

except BankError as e:
    print(e)


'''
class BankError(Exception):

    def __init__(self, message):
        super().__init__(message)


class BankAccount:

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, money):
        if money <= 0:
            raise BankError('{}원 입금 불가'.format(money))
        self.balance += money

    def withdraw(self, money):
        if money <= 0:
            raise BankError('{}원 출금 불가'.format(money))
        if money > self.balance:
            raise BankError('잔액 부족')
        self.balance -= money

    def inquiry(self):
        print('계좌번호: {}'.format(self.acc_no))
        print('통장잔액: {}원'.format(self.balance))

me = BankAccount('012-34-56789', 50000)
you = BankAccount('987-65-43210', 50000)

try:
    print('===이체전===')
    me.inquiry()
    you.inquiry()
    me.withdraw(5000)
    you.deposit(5000)
    print('===이체후===')
    me.inquiry()
    you.inquiry()

except BankError as e:
    print(e)
'''