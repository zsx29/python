# (1) 클래스 정의

from Ch06.Sub01.Account import Account


class StockAccount(Account):  # Account 를 참조한다.

    def __init__(self, bank, id, name, money, stock, amount, price):
        # 부모클래스 생성자 실행(super())
        super().__init__(bank, id, name, money)  # 부모에게 상속 받으면 의무가 생긴다. => 자식이 멤버를 초기화 해줘야한다.
        self.stock = stock
        self.amount = amount
        self.price = price

    def sell(self, amount, price):
        print("{}를 {}가격에 판매함".format(self.stock, amount, price))

    def buy(self, amount, price):
        print("{}를 {}가격에 판매함".format(self.stock, amount, price))


    def show(self):
        super().show()
        print("주식종목: ", self.stock)
        print("주식수량: ", self.amount)
        print("주식가격: ", self.price)
