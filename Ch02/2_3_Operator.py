"""
날짜 : 2021/04/26
이름 : 박재형
내용 : 파이썬 연산자 자료형 실습하기 교재 p38
"""

# 대입연산자------------------------
a = 1
b = c = d = 0
e, f, g = 7, True, "Apple"

print("a:", a)
print("c:", c)
print("f:", f)
print("g:", g)
print("e:", e)

# 산술연산자------------------------
num1 = 1
num2 = 2
num3, num4 = 3, 4

r1 = num1 + num2
r2 = num1 - num2
r3 = num1 * num2
r4 = num4 / num2
r5 = num4 // num2 #몫이 정수
r6 = num4 % num3  #나머지
r7 = num4 ** num3 #제곱

print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r7:", r7)

# 복합대입연산자---------------------
num5, num6, num7, num8 = 5, 6, 7, 8

num5 += 1 # num5 = num5 + 1
num6 -= 2 # num6 = num6 - 2
num7 *= 3 # num7 = num7 * 3
num8 /= 4 # num8 = num8 / 4

print("num5:", num5)
print("num6:", num6)
print("num7:", num7)
print("num8:", num8)

# 비교연산자------------------------
var1 = 1
# 변수1 = 자료1 를 할당한다. 왜? 연산하기 위해
var2 = 2

rs1= var1 > var2  # var1 이 var2 보다 크다.
rs2= var1 < var2  # var1 이 var2 보다 작다.
rs3= var1 >= var2 # var1 이 var2 보다 크거나 같다.
rs4= var1 <= var2 # var1 이 var2 보다 작거나 같다.
rs5= var1 == var2 #참.
rs6= var1 != var2 #거짓.

print(rs1)
print(rs2)
print(rs3)
print(rs4)
print(rs5)
print(rs6)

# 논리연산자------------------------
var3 = 3
var4 = 4

res1 = (var3 > 2) and (var4 > 3) #var3 는 2보다 크다 그리고 var4는 3보다 크다.
res2 = (var3 > 2) or (var4 > 6)  #var3 는 2보다 크다 또는 var4는 6보다 크다.
res3 = (var3 > 2) and (var4 > 6) #var3 는 2보다 크고 그리고 var4는 6보다 크다.
res4 = not (var3 > var4) #var3은 var4보다 크지 않다.
print("res1 :", res1)
print("res2 :", res2)
print("res3 :", res3)
print("res4 :", res4)
# and 연산은 둘다 참이어야 참이 나온다.
# or 연산은 둘 중 하나가 참이면 참이 나온다.

# 대입연산자------------------------

