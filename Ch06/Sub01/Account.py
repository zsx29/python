# (1) 클래스 정의 : 대문자로 정의한다.
class Account:
    # 속성(정보(data))
    def __init__(self, bank, id, name, money):  # __init__ : 생성자 , self : member
        self.__bank = bank  # __ : 캡슐화(보호)
        self.__id = id
        self.__name = name
        self.__money = money

    # 기능
    def deposit(self, money):  # 입금
        self.__money += money

    def withdraw(self, money):  # 출금
        self.__money -= money

    def show(self):  # 잔액조회
        print("-----------------")
        print("은행명 : ", self.__bank)
        print("계좌번호 : ", self.__id)
        print("입금주 : ", self.__name)
        print("현재잔액 : ", self.__money)
