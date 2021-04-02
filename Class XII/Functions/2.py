def vol(l=1, b=1, h=2):
    return l * b * h


l = float(input("ENTER LENGTH\n >> "))
b = float(input("ENTER BREADTH\n >> "))
h = float(input("ENTER HEIGHT\n >> "))

print(f'Volume is {vol(l,b,h)}')
