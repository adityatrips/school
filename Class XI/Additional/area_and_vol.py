from math import pi

print("+--------------------------------+")
print("|   Area and Volume Calculator   |")
print("+--------------------------------+")
print("1. Cube")
print("2. Cuboid")
print("3. Sphere")
print("4. Cylinder")
print("5. Cone")
print("6. Exit")

ch = int(input("Enter your choice\n=> "))

if ch == 1:
  side = float(input("Enter the side\n=> "))
  print("1. Area")
  print("2. Volume")
  av = int(input("Enter your choice again\n=> "))
  if av == 1:
    print(f"Area is {6*(side**2)}")
  elif av == 2:
    print(f"Volume is {side**3}")
  else:
    print("Did I mention any other option!?")

elif ch == 2:
  l = float(input("Enter the length\n=> "))
  b = float(input("Enter the breadth\n=> "))
  h = float(input("Enter the height\n=> "))
  print("1. Area")
  print("2. Volume")
  av = int(input("Enter your choice again\n=> "))
  if av == 1:
    print(f"Area is {2*((l*b)+(b*h)+(l*h))}")
  elif av == 2:
    print(f"Volume is {l*b*h}")
  else:
    print("Did I mention any other option!?")

elif ch == 3:
  r = float(input("Enter the radius\n=> "))
  print("1. Area")
  print("2. Volume")
  av = int(input("Enter your choice again\n=> "))
  if av == 1:
    print(f"Area is {4*pi*(r**2)}")
  elif av == 2:
    print(f"Volume is {(4/3)*pi*(r**3)}")
  else:
    print("Did I mention any other option!?")

elif ch == 4:
  h = float(input("Enter the height\n=> "))
  r = float(input("Enter the radius\n=> "))
  print("1. Area")
  print("2. Volume")
  av = int(input("Enter your choice again\n=> "))
  if av == 1:
    print(f"Area is {2*pi*r*(r+h)}")
  elif av == 2:
    print(f"Volume is {pi*(r**2)*h}")
  else:
    print("Did I mention any other option!?")

elif ch == 5:
  s = float(input("Enter the slant height\n=> "))
  r = float(input("Enter the radius\n=> "))
  print("1. Area")
  print("2. Volume")
  av = int(input("Enter your choice again\n=> "))
  if av == 1:
    print(f"Area is {pi*r*(r+s)}")
  elif av == 2:
    print(f"Volume is {pi*r*s}")
  else:
    print("Did I mention any other option!?")

elif ch == 6:
  print("Why did you even come here!?")

else:
  print("Did I mention any other option!?")
