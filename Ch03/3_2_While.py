"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 while 실습 교재 p60
"""

num1 = 1

while num1 < 5:
    print("num1 : ", num1)
    num1 += 1

# 1부터 10까지 합

k, sum = 1, 0

while k <= 10:
    sum += k
    k += 1

print("1부터 10까지 합: ", sum)

# 1부터 10까지 짝수 합

i, tot = 1, 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
print("1부터 10까지 짝수 합: ", tot)

# Break #

num = 1

while True:
    if num % 5 == 0 and num % 7 == 0:
        # 반복문 종료
        break
    num += 1

print("5와 7의 최소공배수 : ", num)

# Continue #

s, total = 1, 0

while s <= 10:
    s += 1
    if s % 2 == 1:
        continue

    total += s

print("1부터 10까지 짝수 합 : ", total)












