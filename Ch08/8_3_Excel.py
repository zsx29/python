"""
날짜 : 2021/05/03
이름 : 박재형
내용 : 파이썬 외부파일 설치 실습 교재 p239
"""

from openpyxl import Workbook  # 엑셀패키지 불러오기

# Excel 파일 쓰기

# (1) 엑셀파일 객체생성
workbook = Workbook()

# (2) 활성화된 sheet 선택
sheet = workbook.active

# (3) 데이터 입력
sheet["A1"] = "홍길동" # A열에 1째 행
sheet.append([1, 2, 3])
sheet.append(["김유신", "김춘추", "장보고"])
sheet.cell(6, 2, "사과")

# (4) 엑셀파일 저장, 닫기
workbook.save("C:/Users/bigdate/Desktop/Sample.xlsx")
workbook.close()

print("작업완료")