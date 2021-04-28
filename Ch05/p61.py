# 단일 조건문

var = 10
if var >= 5:
    print("var :", var)
    print("var는 5보다 크다.")
    print("조건이 참인 경우 실행")

print("항상 실행")

# 단일 조건문2
# 100~85 우수, 84~70: 보통 69이하 :저조
score = int(input("점수 입력 :"))
if score >= 85 and score <= 100:
    print("우수")
else :
    if score >= 70:
        print("보통")
    else :
        print("저조")