"""
날짜 : 2021-06-03
이름 : 박재형
내용 : 체스 - 나이트 움직이기
"""

input_date = input()
row = int(input_date[1])
column = int(ord(input_date[0])) - int(ord('a')) + 1


result = 0

# 오른쪽 2칸, 위로 1칸
next_row = row + 2
next_col = column - 1

# 체스판 안에 들어와있는지 확인
if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1

# 오른쪽 2칸, 아래 1칸
next_row = row + 2
next_col = column + 1

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1

# 왼쪽 2칸, 위로 1칸
next_row = row - 2
next_col = column - 1

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1
# 왼쪽 2칸, 아래 1칸
next_row = row - 2
next_col = column + 1

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1
# 위로 2칸, 오른쪽 1칸
next_row = row + 1
next_col = column - 2

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1
# 위로 2칸, 왼쪽 1칸
next_row = row - 1
next_col = column - 2

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1
# 아래로 2칸, 오른쪽 1칸
next_row = row + 1
next_col = column + 2

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1
# 아래로 2칸, 왼쪽 1칸
next_row = row - 1
next_col = column + 2

if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
    result += 1

print(row)
print(column)
print("result : ", result)
