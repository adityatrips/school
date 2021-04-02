months = {
  'january': '01',
  'february': '02',
  'march': '03',
  'april': '04',
  'may': '05',
  'june': '06',
  'july': '07',
  'august': '08',
  'september': '09',
  'october': '10',
  'november': '11',
  'december': '12',
}
date = input("ENTER A DATE IN THE FORMAT (DDMMYYYY)\n >> ")
day = date[:2]
month_num = date[2:4]
year = date[-4:]

for key, val in months.items():
  if val == month_num:
    print(f'{key.title()} {day}, {year}')
