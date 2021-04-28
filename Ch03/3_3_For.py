"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 for 실습 교재 p60
"""

# (1) for
for i in range(5):  # range(5) : 5까지 반복
    print("i : ", i)

for j in range(10, 20):  # range(10, 20) : 10~19까지 반복
    print("j : ", j)

for k in range(10, 0, -1):  # range(10, 0, -1) : 10에서 시작 0까지 -1차감
    print("k : ", k)

# (2) 1부터 10까지 합
sum1 = 0

# for sum1 in range(11):


print("1부터 10까지의 합 : ", sum1)

# (3) 1부터 10까지 짝수 합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k

print("1부터 10까지 짝수 합 : ", sum2)

# (4) 중첩 for
for a in range(3):
    print("a :", a)
    for b in range(4):
        print("b :", b)
        pass

# (5) 구구단
for x in range(2, 10):
    print(x, "단")
    for y in range(1, 10):
        z = x * y
        print(x, y, z)
# (6) 별삼각형
for a in range(10, 0, -1):
    for b in range(a):
        print("☆", end="")
    print()

for i in range(10):
    print("★" * i)

# (7) List 를 이용한 for - I
nums = [1, 2, 3, 4, 5]

for num in nums:
    print("num :", num)

for person in ["김유신", "김춘추", "장보고"]:
    print("person :", person)

score = [62, 42, 56, 72, 12]
total = 0

# (8) List index, value 출력
for index, value in enumerate(score):
    print("{}, {}".format(index, value))

# (9) List 를 comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [num * 2 for num in list1]
list3 = [num * 3 for num in list1 if num % 2 == 1]
print("list2 :", list2)
print("list3 :", list3)
