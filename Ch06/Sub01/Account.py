# (1) 클래스 정의 : 대문자로 정의한다.
class Account:
    # 속성(정보(data))
    def __init__(self, bank, id, name, money):  # __init__ : 생성자 , self : member
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money

    # 기능
    def deposit(self, money):  # 입금
        self.money += money

    def withdraw(self, money):  # 출금
        self.money -= money

    def show(self):  # 잔액조회
        print("-----------------")
        print("은행명 : ", self.bank)
        print("계좌번호 : ", self.id)
        print("입금주 : ", self.name)
        print("현재잔액 : ", self.money)
