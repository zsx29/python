"""
날짜 : 2021/04/30
이름 : 박재형
내용 : 최댓값 최솟값 문제
"""

scores = [62, 82, 76, 88, 54, 92]

max = scores[0]
min = scores[0]

for score in scores:
    if max < score:
        max = score
    if min > score:
        min = score

print("최댓값 :", max)
print("최솟값 :", min)
