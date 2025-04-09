from openpyxl import load_workbook

workbook = load_workbook('livros.xlsx')
sheet = workbook.active

column = sheet['A'] 
for cell in column:
    value = cell.value
    print(value)
