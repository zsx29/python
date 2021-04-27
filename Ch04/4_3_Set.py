"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 자료구조 Set 실습 교재 p96
"""
# Set = 집합주머니, 순서X, 중복X

# Set 생성 #
set1 = {1, 2, 3, 4, 5, 3}

print(type(set1))
print(set1)
# 3은 중복값이라 출력되지 않음.

set2 = set("hello world!")

print(type(set1))
print(set2)
# 개별적인 문자로 출력, 스페이스도 문자로 취급 = " ", 순서도 없음

# Set 출력 = List 변환 후 출력 #
list1 = list(set1)
print(list1)

list2 = list(set2)
print(list2)




























