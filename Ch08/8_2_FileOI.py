"""
날짜 : 2021/05/03
이름 : 박재형
내용 : 파이썬 파일 입출력 실습 교재 p217
"""

# (1) 파일 읽기(File-Input)
# 파일을 읽어올 경로가 필요하다.(파이썬에서 \ ==> / 변환)
# 파일을 열었으면 닫아줘야한다. (open() --> close())

file1 = open('C:/Users/bigdate/Desktop/Sample.txt', 'r')  # "r" : read(mode)
line = file1.readline()

print(line)
file1.close()

# (2) 여러줄 파일 읽기
file2 = open('C:/Users/bigdate/Desktop/Sample.txt', 'r')

while True:
    line = file2.read()

    if not line:
        # 읽을 라인이 없을 경우
        break

    print(line)

file2.close()

# (3) 파일 쓰기(File-Output)
# 가상경로
file3 = open('C:/Users/bigdate/Desktop/Test.txt', 'w')  # "w" = write(mode)
file3.write("안녕하세요\n")
file3.write("안녕하세요1\n")
file3.write("안녕하세요2\n")
file3.write("안녕하세요3\n")
file3.close()

# (4) 구구단 쓰기
file4 = open('C:/Users/bigdate/Desktop/gugudan.txt', 'w')
for i in range(2, 10):
    file4.write("~~~~~~{}단~~~~~~\n".format(i))
    for j in range(1, 10):
        file4.write("%d x %d = %d\n" % (i, j, i * j))

file4.close()
