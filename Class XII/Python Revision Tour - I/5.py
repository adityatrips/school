import datetime

x = int(input("ENTER A NUMBER TO SEE THE DAY\n >> "))

while x not in range(2,366):
  print("Invalid number")
  x = int(input("ENTER A NUMBER TO SEE THE DAY\n >> ")).lower()

dayname = input("ENTER THE FIRST DAY IN THE YEAR\n >> ").lower()

daynames = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

while dayname not in daynames:
  print("Invalid day name")
  dayname = input("ENTER THE FIRST DAY IN THE YEAR\n >> ")

rslt = daynames[(daynames.index(dayname) + x) % 7]

print(rslt)