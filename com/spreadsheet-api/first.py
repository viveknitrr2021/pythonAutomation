import gspread

gc = gspread.service_account('secret.json')

spreadsheet = gc.open('weather_public')

worksheet1 = spreadsheet.get_worksheet(0)
data = worksheet1.get_values('A5:F7')
print(data)

# worksheet1.update('E5', -29)

worksheet1.update_cell(5, 5, -190)