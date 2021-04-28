"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 조건문 if 실습 교재 p60
"""

# if #
num1, num2 = 1, 2

if num1 > 0:
    print("num1은 0보다 크다")

if num1 > num2:
    print("num1 은 num2보다 크다.")

if num1 > 0:
    if num2 > 1:
        print("num1은 0보다 크고, num2 는 1보다 크다.")

if num1 > 0 and num2 > 1:
    print("num1은 0보다 크고, num2 는 1보다 크다.")

# if else #

num3, num4 = 3, 4

if num3 > num4:
    # 조건이 참일 떄
    print("num3 가 num4 보다 크다")
else:
    # 조건이 거짓일 떄
    print("num3 가 num4 보다 작다")

# if ~ elif ~ else #

if num1 > num2:
    print("num1 은 num2 보다 크다")
elif num2 > num3:
    print("num1 은 num2 보다 크다")
elif num3 > num4:
    print("num1 은 num2 보다 크다")
else:
    print("num4가 가장 크다.")

# 삼항조건문 #
num = 5
result = num * 2 if num >= 5 else num + 2
# 참이면 앞쪽 연산, 거짓이면 뒤쪽 연산

print(result)

# Test #
score = int(input("점수 입력 : "))
print("점수 확인 : ", score)

if score >= 90 and score < 100:
    print("A 입니다.")
elif score >= 80 and score < 90:
    print("B 입니다.")
elif score >= 70 and score < 80:
    # 70 >= score < 80
    print("C 입니다.")
elif score >= 60 and score < 70:
    print("D 입니다.")
else:
    print("F 입니다.")
