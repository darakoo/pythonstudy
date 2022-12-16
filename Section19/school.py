import openpyxl as oxl

# 엑셀파일 로드
wb = oxl.load_workbook('./Section19/score.xlsx')
org_ws = wb['Sheet1']

# sheet 복사후 sheet 이름 설정
cpy_ws = wb.copy_worksheet(org_ws)
# cpy_ws.title = 'copy_sheet'       # sheet 이름을 지정해도 된다.

# 파일 저장
wb.save('./Section19/score.xlsx')
print(wb.sheetnames)