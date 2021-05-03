"""
날짜 : 2021/05/03
이름 : 박재형
내용 : 파이썬 예외처리 실습 교재 p212
"""

# (1) try ~ except
num1, num2 = 1, 0
r1 = r2 = r3 = r4 = 0

try:
    # 예외가 발생할 가능성이 있는 로직 코드영역
    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num1 * num2
    r4 = num1 / num2
except:
    # 예외가 발생했을 때 처리할 코드영역
    print("예외발생...")

print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)
print("r4 :", r4)

# (2) try ~ except ~ finally
people = ["김유신", "김춘추", "장보고"]

try:
    # 예외(error)가 발생 할 가능성이 있는 코드영역
    for i in range(3):  # i : 0, 1, 2, 3
        print(people[i])

except IndexError:
    # 예외(error)가 발생했을 때 처리할 코드영역
    print("유효하지 않는 인덱스 참조")
finally:
    # 예외(error) 발생여부 관계없이 마지막에 실행되는 코드영역
    print("예외처리 완료")

# (3) try ~ except ~ else
animal = ["사자", "코끼리", "호랑이", "기린"]
result = None

while True:
    try:
        # 예외(error)가 발생 할 가능성이 있는 코드영역
        print("동물을 선택하시오.")
        print("1:사자, 2:코끼리, 3:호랑이, 4:기린, 0:종료")

        answer = int(input("선택 : "))

        if answer == 0:
            break
        elif answer < 0:
            # 예외 일으키기(던지기)
            raise Exception("양수를 입력하시오.")  # 인위적으로 에러를 일으킨다(raise)

        result = animal[answer - 1]

    except Exception as e:
        # 예외(error)가 발생했을 때 처리할 코드영역
        print("에러 내용 :", e)
        print("1 ~ 4 사이의 수를 입력하시오.")

    else:
        # 예외(error)가 발생 안했을 때 실행되는 코드영역
        print("선택한 동물 :", result)

print("프로그램 종료...")
