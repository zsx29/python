"""
날짜 : 2021-05-24
이름 : 박재형
내용 : 코딩 테스트 04 - 1이 될때 까지
"""

n = int(input())

x, y = 1, 1
plans = input().split()

for plan in plans:
    if plan == "R":
        if y == n:
            continue
        else:
            y += 1
    if plan == "L":
        if y == 1:
            continue
        else:
            y -= 1
    if plan == "U":
        if x == 1:
            continue
        else:
            x -= 1
    if plan == "D":
        if x == n:
            continue
        else:
            x += 1


print(x, y)