import openpyxl

wb = openpyxl.load_workbook('./google.xlsx')
sheet = wb['설문지 응답 시트1']
a = sheet['A2':'T3']
row_list = []
all_values = []
for row in a:
    for cell in row:
        row_list.append(cell.value)
    # all_values.append(row_list)
print(row_list)