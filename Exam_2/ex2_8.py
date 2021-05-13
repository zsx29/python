"""
날짜 : 2021-05-13
이름 : 박재형
내용 : 파이썬 정규 표현식 연습문제.
"""

from re import findall, sub

texts_re1 = ["abc동해물과 123백두산이 eafa마르고 456닳도록789", "^하느님이 보우하사! !@# 우리나라 만세&&"]
print("text_re1", texts_re1)

# 숫자 제거
texts_re2 = [sub("[0-9]", "", text) for text in texts_re1]
print("texts_re2 :", texts_re2)

# 특수문자 제거
texts_re3 = [sub("[!@#$%^&]", "", text) for text in texts_re2]
print("texts_re3 :", texts_re3)

# 영문자 제거
texts_re4 = [sub("[a-z|A-Z]", "", text) for text in texts_re3]
print("texts_re4 :", texts_re4)