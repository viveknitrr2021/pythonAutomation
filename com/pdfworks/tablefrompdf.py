import tabula

table = tabula.read_pdf('D:/pythonAutomation/com/resources/weather.pdf', pages=1)
# print(table)

table[0].to_csv('outputted.csv', index=None)