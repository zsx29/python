"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 캡슐화 실습 교재 p161
"""

from Ch06.Sub01.Account import Account

kb = Account("국민은행", "101-15-6494465-0", "김유신", 30000)
kb.deposit(10000)
kb.withdraw(5000)

# 캡슐화(정보은닉)을 적용해서 취약코드를 예방!
# kb.money -= 1  # 캡슐화가 되어 있어서 참조를 못한다.

kb.show()
