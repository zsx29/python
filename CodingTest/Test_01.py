"""
날짜 : 2021-05-13
이름 : 박재형
내용 : 파이썬 코딩테스트 1번
"""

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# -----------------------------------------

# 리스트를 내림차순으로 정렬
data.sort(reverse=True)
# 가장 큰 수
first = data[0]
# 두번째 큰 수
second = data[1]

result = 0
# k를 보존하기위해 repeat에 담아둔다.
repeat = k

for i in range(m):

    if repeat > 0 :
        result += first
        repeat -= 1
    else:
        result += second
        repeat = k

# 최종 답안 출력
print("result :", result)
