import tabula
# use pip install tabula-py,openpyxl.
table = tabula.read_pdf('weather.pdf', pages=1)

print(table[0])

table[0].to_excel('output.xlsx', index=None)