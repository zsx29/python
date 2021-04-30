# 딕트 객체 예

# (1) dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성 방법2
person = {"name":"홍길동", "age": 26, "address":"부산시"}
print(person)
print(person["name"])
print(type(dic), type(person))

# (3) 원소 수정, 삭제, 추가
person["age"] = 21
print(person)

del person["address"]
print(person)
person["pay"] = 250
print(person)

# 요소 검사

# (1) 요소 검사
print(person["age"])
print("age" in person)

# (2) 요소 반복
print("---------요소 반복--------------")
for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)