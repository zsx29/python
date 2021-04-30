"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 Class(객체지향) 실습 교재 p148
"""
# (1) 불러오기
from Ch06.Sub01.Account import Account  # 출처를 달아준다.
from Ch06.Sub01.Computer import Computer

# (2) 객채생성
kb = Account("국민은행", "101-10-100154", "박재형", 10000)  # 클래스의 함수를 실행(__init__), kb : 객체
kb.deposit(40000)  # . : 참조연산자
kb.withdraw(7000)
kb.show()

wr = Account("우리은행", "010-2244-211285", "김춘추", 30000)
wr.deposit(40000)
wr.withdraw(3000)
wr.show()

samsung = Computer("삼성", "intel i7", "16GB", "1TB")
apple = Computer("애플", "intel i5", "32GB", "2TB")

samsung.info()
apple.info()
