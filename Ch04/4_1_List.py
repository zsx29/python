"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 자료구조 List 실습 교재 p84
"""

# List 생성 #
list1 = [1, 2, 3, 4, 5]
print("list type : ", list1)
print("list1[0] : ", list1[0])
print("list1[1] : ", list1[1])
print("list1[2] : ", list1[2])
print("list1[3] : ", list1[3])
print("list1[4] : ", list1[4])

list2 = [5, 3.14, True, "Apple"]
print("list2 type : ", type(list2))
print("list2[0]", list2[1])
print("list2[1]", list2[2])
print("list2[2]", list2[3])

# list in list
list3 = [[1, 2, 3]
        ,[4, 5, 6]
        ,[7, 8, 9]]

print(type(list3))
# list3 안의 [행]의 [열]
print(list3[0][0])
print(list3[0][1])
print(list3[0][2])
print(list3[2][1])

# List 덧셈 #
animal1 = ["사자", "호랑이", "강아지", "고양이"]
animal2 = ["곰", "기린"]

result = animal1 + animal2
print(result)

# List 수정, 추가, 삭제 #
nums = [1, 2, 3, 4, 5]

# 추가
nums[0] = "헬로"
print(nums)

# [2:4] = 2~4까지 수정
nums[2:4] = [8, 9, 10]
print(nums)

# [3:5] = 3~4까지 삭제
nums[3:5] = []
print(nums)















