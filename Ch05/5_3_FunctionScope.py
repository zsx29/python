"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 function scope 실습 교재 p132
"""


def sum(x, y):
    tot = 0

    for k in range(x, y+1):
        tot += k
    return tot


tot = 0
start = 1
end = 10

tot = sum(start, end)
print("tot :", tot)
