# 표준출력장치

# (1) value 인수
print("value : ", 10 + 20 + 30 + 40 + 50)

# (2) sep 인수 : 값과 값을 특수문자로 구분
print("010", "9214", "8036", sep="-")

# (3) end 인수
print("value : ", 10, end=", ")
print("value : ", 20)

# (4) format()함수 인수 : format(value, "format")
print("원주율 : ", format(3.14159, "8.3f"))
# 전체 8개 자릿수를 기준으로 소수점 이하 3째 자리까지 표시된다.
print("금액 : ", format(10000, "10d"))
print("금액 : ", format(125000, "3,d"))

# (5) 양식문자 인수 : print(" %양식문자" %(값))
name = "박재형"
age = 27
price = 123.456
print("이름 : %s, 나이 : %d, date = %.2f" %(name, age, price))

# (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, date = {}".format(name, age, price))