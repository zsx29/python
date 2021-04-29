"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 function builtin(내장함수) 실습 교재 p118
"""

# 수학관련 #
# abs() : 절대값을 구하는 함수

r1 = abs(-5)
print(r1)

# ceil() : 올림 함수
import math
import random
import time

r2 = math.ceil(1.2)
r3 = math.ceil(1.8)
print(r2, r3)

# floor() : 내림 함수

r4 = math.floor(1.2)
r5 = math.floor(1.8)
print(r4, r5)

# round() : 반올림 함수
r6 = round(1.2)
r7 = round(1.8)
print(r6, r7)

# sqrt() : 제곱근
r8 = math.sqrt(4)
r9 = math.sqrt(9)
print(r8, r9)

# random

num1 = random.random()  # 0 ~ 1 사이의 실수
print(num1)

num2 = num1 * 10
print(num2)  # 0 ~ 10 사이의 실수

num3 = math.ceil(num2)
print(num3)  # 1 ~ 10 사이의 정수

# 코드 중첩
num4 = math.ceil(random.random() * 10)
print(num4)  # 1 ~ 10 사이의 정수

# 날짜, 시간
t1 = time.time()
print("t1 :", t1)  # unix time

# 날짜, 시간을 구하는 기본적인 방법
t2 = time.ctime()
print("날짜, 시간은 :", t2)

now = time.localtime(time.time())
year = time.strftime("%Y", now)
month = time.strftime("%m", now)
date = time.strftime("%d", now)
hour = time.strftime("%H", now)
min = time.strftime("%M", now)
sec = time.strftime("%S", now)

print("---- 현재 시간 ----")
print("%s년 %s월 %s일" % (year, month, date))
print("%s시 %s분 %s초" % (hour, min, sec))










