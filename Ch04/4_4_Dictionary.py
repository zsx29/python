"""
날짜 : 2021/04/27
이름 : 박재형
내용 : 파이썬 자료구조 Dictionary 실습 교재 p98
"""

# Dictionary 생성
dic1 = {1: "서울", 2: "대전", 3: "대구", 4: "부산", 5: "광주"}
dic2 = {
    "a":"apple",
    "b":"banana",
    "c":"cherry"
}
dic3 = {
    101:[1, 2, 3, 4, 5],
    102:(6, 7, 8, 9, 10),
    103:{"한국", "미국", "중국", "일본"},
    104:{"p1": "김유신", "p2": "이순신", "p3": "장보고"}
}

# Dictionary 출력
print(type(dic1))
print(dic1[1])
print(dic1[3])
print(dic1[4])

print(dic2["a"])
print(dic2["b"])
print(dic2["c"])

print(dic3[101][1])
print(dic3[102][2])
print(dic3[103])
print(dic3[104]["p2"])

# Dictionary 응용 #
dics = [dic1, dic2, dic3]

print(type(dics))
print(dics[0][3])
print(dics[1]["a"])
print(dics[2][104]["p2"])






















