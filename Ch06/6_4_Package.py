"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 패키지와 모듈 실습 교재 p175
"""
# 참조 v01
import Ch06.Sub02.calc as c  # c : 별칭을 준다.(마음대로)

# 참조 v02
from Ch06.Sub02.calc import *

r1 = c.plus(1, 2)
r2 = c.minus(2, 3)
r3 = multi(3, 4)
r4 = div(4, 2)

print("r1: ", r1)
print("r2: ", r2)
print("r3: ", r3)
print("r4: ", r4)
