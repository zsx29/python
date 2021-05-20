"""
날짜 : 2021/04/30
이름 : 박재형
내용 : 최댓값 선택정렬 문제
"""

dataset = [3, 5, 1, 2, 4]
size = len(dataset)

for i in range(size-1):
    for j in range(i+1, size):

        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print("%d Round: %s" % (i, dataset))

print("result: ", dataset)