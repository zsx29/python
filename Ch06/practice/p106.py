# 선택정렬 알고리즘

# (1) 오름차순 정렬
dataset = [3, 5, 1, 2 ,4]
n = len(dataset)
for i in range(1, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset)