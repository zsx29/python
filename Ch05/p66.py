# 무한 루프
numdata = []

while True:
    num = int(input("숫자 입력 :"))

    if num % 10 == 0:
        print("프로그램 종료")
        break
    else:
        print(num)
        numdata.append(num)
# append : 추가하다.