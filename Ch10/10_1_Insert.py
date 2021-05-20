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
sql = "INSERT INTO `USER1` VALUES ('A101','김유신','010-9214-8036', 27);"
cur.execute(sql)
conn.commit()

# (4) 데이터베이스 종료
conn.close()

print("insert 완료")

