"""
날짜 : 2021/04/30
이름 : 박재형
내용 : 파이썬 기본 입출력
"""

# 이름 ,나이, 생년월일 출력

name = input("이름을 입력하시오: ")
age = input("나이을 입력하시오: ")

year = 2021 - int(age)

print(name + "님은" + age + "세 이고," + str(year) + "년도에 태어 났습니다.")

# 평균 계산 출력
n1 = int(input("첫 번째 숫자 입력 :"))
n2 = int(input("두 번째 숫자 입력 :"))
n3 = int(input("세 번째 숫자 입력 :"))


mean = (n1 + n2 + n3) / 3
print(n1, n2, n3, "의 평균은", mean, "입니다.")1