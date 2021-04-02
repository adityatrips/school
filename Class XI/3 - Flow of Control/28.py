temp = float(input("ENTER CURRENT TEMPERATURE\n=> "))
unit = input(
    "WHAT UNIT DO YOU WANNA CHOOSE [c]elsius or [f]ahrenheit\n=> "
).lower()

if unit == 'c':
  temp_f = (5/9)*(temp-32)
  print(f'The converted temperature from celsius to fahrenheit is: {temp_c}')
else:
  temp_c = ((9/5)*c)+32
  print(f'The converted temperature from fahrenheit to celsius is: {temp_f}')
