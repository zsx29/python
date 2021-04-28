# range 클래스 예

# (1) range 객체 생성
num1 = range(10)
print(num1)

num2 = range(1, 10, 2)  # range(start, stop, step)
# (2) range 객체 활용
for n in num1:
    print(n, end=" ")
    print()

for n in num2:
    print(n, end=" ")
    print()
