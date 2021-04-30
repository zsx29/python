"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 클래스 상속 실습 교재 p163
"""

from Ch06.Sub02.StockAccount import StockAccount

kb = StockAccount("kb증권", "110-12-545455-0", "박재형", 10000, "삼성전자", 12, 80000)
kb.deposit(40000)
kb.withdraw(5000)
kb.buy(10, 80000)
kb.sell(10, 30000)
kb.show()  # 부모의 show()까지 override
