# break, continue

i = 0
while i < 10:
    i += 1  # 카운터
    if i == 3:
        continue  # 다음문장 스킵
    if i == 6:
        break
    print(i, end=" ")