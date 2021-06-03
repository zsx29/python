"""
날짜 : 2021-06-03
이름 : 박재형
내용 : 시각
"""

# h값 입력받기
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print("result : ", count)
