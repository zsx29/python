# 셋 객체 예

# (1) 중복 불가
s= {1, 3, 5, 3, 1}
print(len(s))
print(s)

# (2) 요소 반복
for d in s:
    print(d, end=" ")
    print()

# (3) 집합관련 함수
s2 = {3, 6}
print(s.union(s2))  # 합집합
print(s.difference(s2))  # 차집합
print(s.intersection(s2))  # 교집합

# (4) 추가, 삭제 함수
s3 = {1, 3, 5}
print(s3)
s3.add(7)
print(s3)
s3.discard(3)
print(s3)

