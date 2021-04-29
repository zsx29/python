# 추가, 삭제, 수정, 삽입 예

# (1) 단일 리스트 객체 생성
num = ["one", "two", "three", "four"]
print(num)
print(len(num))

# (2) 리스트 원소 추가
num.append("five")
print(num)
print(len(num))

# (3) 리스트 원소 삭제
num.remove("five")
print(num)

# (4) 리스트 원소 수정
num[3] = "4"
print(num)

# (5) 리스트 원소 삽입
num.insert(0, "zero")
print(num)
print(len(num))

# 추가, 삭제, 수정, 삽입 예시
print("--------------------------------")
# (1) 리스트 결합
x = [1, 2, 3, 4]
y = ["a", "b", "c"]
z = x + y
print(z)


# (2) 리스트 확장
x.extend(y)  # x 추가
print(x)

# (3) 리스트 추가
x.append(y)
print(x)

# (4) 리스트 두배 확장
lst = [1, 2, 3, 4]
result = lst * 2
print(result)