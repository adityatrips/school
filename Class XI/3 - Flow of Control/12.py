a = float(input("ENTER SIDE A\n=> "))
b = float(input("ENTER SIDE B\n=> "))
c = float(input("ENTER SIDE C\n=> "))

if a == b == c:
  print("Triangle is equilateral")
elif a == b or b == c or c == a:
  print("Triangle is isosceles")
else:
  print("Triangle is scalene")
