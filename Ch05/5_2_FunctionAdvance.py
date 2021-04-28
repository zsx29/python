"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 function 고급 함수 실습 교재 p129
"""


# default 매개변수
def hello(name="홍길동", age=21):
    print("이름 :", name)
    print("나이 :", age)


hello()
hello("김유신")
hello("김춘추", 31)


# 가변 매개변수
def total(*nums):  # nums : list
    tot = 0
    for n in nums:
        tot += n

    return tot


r1 = total(1)
r2 = total(1, 2)
r3 = total(1, 2, 3)
print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)


# 하나 이상의 리턴값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2
    return y1, y2


rs1, rs2 = sum_and_multi(1, 2)
rs3, rs4 = sum_and_multi(3, 4)
print("rs1 : %d, rs2 : %d" % (rs1, rs2))
print("rs3 : %d, rs4 : %d" % (rs3, rs4))


# 변수에 저장하는 함수
def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


var1 = plus
var2 = minus

res1 = var1(1, 2)
res2 = var2(2, 3)
# var1에 있는 함수를 실행

print("res1 :", res1)
print("res2 :", res2)

cals = [plus, minus]
res3 = cals[0](3, 4)
res4 = cals[1](4, 5)

print("res3 :", res3)
print("res4 :", res4)
# 람다함수(익명함수) : 함수인데 이름이 없음
lam_plus = lambda x, y: x + y  # x, y : 매개변수 x + y : 리턴값
result = lam_plus(2, 3)
print("result :", result)