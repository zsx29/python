"""
날짜 : 2021/04/29
이름 : 박재형
내용 : 파이썬 function list함수 실습 교재 p88
"""

dataset = [1, 4, 3]
print("1.dataset: ", dataset)

# 리스트 원소 추가 : .append() : (자주사용)
dataset.append(2)
dataset.append(5)
print("2.dataset: ", dataset)

# 리스트 정렬
dataset.sort()
print("3.dataset: ", dataset)  # 오름차순

dataset.sort(reverse=True)
print("4.dataset: ", dataset)  # 내림차순

# 리스트 원소 삽입
dataset.insert(2, 6)  # index 2번째 자리에 6 삽입
print("5.dataset: ", dataset)

# 리스트 원소 삭제
dataset.remove(6)  # 해당원소 삭제
print("6.dataset: ", dataset)


# map 함수 : 일괄적용한다.
# 리스트 원소를 지정된 함수로 일괄 처리해주는 함수
# 여러 개의 데이터를 한번에 다른 형태로 변환할 때 많이 사용한다.
def plus10(n):
    return n + 10


# (1)
list1 = [1, 2, 3, 4, 5]
list_map = map(plus10, list1)
list1_map_list = list(map(plus10, list1))  # list1의 원소에 plus10 함수를 일괄 적용한다.
print("list1_map_list: ", list1_map_list)

# (2)
list2 = [1.1, 2.2, 3.3, 4.4, 5.5]
list2_map_list = list(map(int, list2)) # list2의 원소에 int 함수를 일괄 적용한다.
print("list2_map_list: ", list2_map_list)

# (3)
list3 = [1, 2, 3, 4, 5]
list3_map_list = list(map(lambda x:x*2, list3))
print("list3_map_list: ", list3_map_list)

# (4)
list4 = ["1", "2", "3", "4", "5"]
# int함수는 문자 --> 숫자, 실수 --> 정수
list4_map_list = list(map(int, list4))
print("list4_map_list: ", list4_map_list)
print(type(list4_map_list[1]))

# input 함수 확장
a = input("입력 :")
print("a: ", a)

var1, var2, var3 = map(int, input("3개 숫자 입력(띄어쓰기 구분) :").split())  # .split() :  1개 이상의 입력값을 동시에 받는다.
print("var1: {}, var2: {}, var3: {}".format(var1, var2, var3))
print("var1 + var2 + var3 :", var1+var2+var3)














