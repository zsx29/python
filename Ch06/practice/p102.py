# 객체 주소 복사

# (1) 객체 주소 복사
name = ["홍길동", "이순신", "강감찬"]
print("name address: ", id(name))

name2 = name  #주소 복사
print("name address: ", id(name2))

name2[0] = "박재형"

import copy
name3 = copy.deepcopy(name)  # 내용은 동일, 주소는 다름
print(name)
print(name3)

print(id(name))
print(id(name3))