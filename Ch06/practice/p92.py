# 리스트 내포 예

# 형식1) 변수 = [ 실행문 for ]
x = [2, 4, 1, 5, 7]
lst= [ i ** 2 for i in x]  # x에 제곱계산
print(lst)

# 형식2) 변수 [ 실행문 for if ]
num = list(range(1, 11))
lst2 = [i * 2 for i in num if i % 2 == 0]
print(lst2)

