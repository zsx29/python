position = ["과장", "부장", "대리", "사장", "대리", "과장"]
var1 = list(set(position))

position_cnt = {}
for p in position:
    position_cnt[p] = position_cnt.get(p, 0) + 1

print("중복x: ", var1)
print("각 직위별 빈도수: ", position_cnt)
