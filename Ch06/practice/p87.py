# 중첩 list 객체 예

# (1) 단일 리스트 객체 생성
a = ["a", "b", "c"]
print(a)

# (2) 중첩 리스트 객체 생성

b = [10, 20, a, 5, True, "문자열"]  # 서로 다른 문자열
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])