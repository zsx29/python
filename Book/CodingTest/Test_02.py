"""
날짜 : 2021-05-13
이름 : 박재형
내용 : 파이썬 코딩테스트 2번
"""

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

nums = []
result = 0

for i in range(n):
    data = list(map(int, input().split()))

    # (1) data에서 가장 작은 수를 구한다.
    data.sort()
    num = data[0]  # 가장 작은 수
    nums.append(num)  # 가장 작은 수를 리스트에 추가
    # 현재 nums = [1, 1, 2]

nums.sort(reverse=True)
# 내림차순으로 정렬 한 후 : [2, 1, 1]
result = nums[0]
# 리스트의 첫번째 수를 출력한다. : nums[0]
print(result)
