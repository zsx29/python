# 함수만 정의해놓은 것 = 라이브러리(모듈)

def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


# print("plus :", plus(1, 2))
# print("minus :", minus(1, 2))

if __name__ == "__main__":
    # 모듈 파일의 시작점
    # 실행목적 : 시작점을 선언해서 의도치 않은 코드실행을 차단한다.
    print("plus :", plus(1, 2))
    print("minus :", minus(1, 2))
    print("multi :", multi(3, 4))
    print("div :", div(4, 2))
