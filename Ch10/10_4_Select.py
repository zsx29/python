"""
날짜 : 2021-05-20
이름 : 박재형
내용 : 파이썬 데이터베이스 SQL 실습
"""

import pymysql

# (1) 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='woguddldla',
                       password='1234',
                       db='woguddldla',
                       charset='utf8')

# (2) SQL 실행 객체 생성
cur = conn.cursor()

# (3) SQL 실행
sql = "SELECT * FROM `USER1`;"
cur.execute(sql)

# (4) 결과출력 : result_list에 리스트 형태로 담아낸다.
result_list = cur.fetchall()
for row in result_list:
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("아이디 : ", row[0])
    print("이름 : ", row[1])
    print("번호 : ", row[2])
    print("나이 : ", row[3])
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

# (5) 데이터베이스 종료
conn.close()

print("삭제 완료")

