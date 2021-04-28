# 랜덤 함수

# (1) 이름 list에 전체 이름, 특정 이름 출력
import random

names = ["홍길동", "이순신", "유관순"]
print(names)  # 전체 출력
print(names[1])  # 특정 이름 출력

# (2) list에서 자료 유뮤 확인하기
if "유관순" in names:
    print("유관순 있음")
else:
    print("유관순 없음")

# (3) 난수 정수로 이름 선택하기
idx = random.randint(0, 2)
print(names[idx])
# names 안의 값을 랜덤으로 출력한다.