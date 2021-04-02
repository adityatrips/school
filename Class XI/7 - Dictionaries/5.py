def add2dict(d, k, v):
  d[k] = v


d = {}

while True:
  prod_name = input("ENTER THE PRODUCT NAME\n=> ")
  prod_price = float(input("ENTER THE PRODUCT PRICE\n=> "))
  add2dict(d, prod_name, prod_price)
  q = input(
      "QUIT ENTERING or PRINT DICTIONARY AND CONTINUE ADDING or START VIEWING(q/p/s)\n=> "
  ).lower()
  if q == 'q':
    break
  elif q == 'p':
    print(d)
  else:
    while True:
      p_name = input("ENTER THE PRODUCT NAME TO GET THE PRICE\n=> ")
      for key, val in d.items():
        if key == p_name:
          print(f'{key} HAS A PRICE OF {val}')
