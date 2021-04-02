rno = []
marks = []

for _ in range(4):
  r, m = eval(input("ENTER ROLL NUMBER, MARKS\n=> "))
  rno.append(r)
  marks.append(m)

d = {
    rno[0]: marks[0],
    rno[1]: marks[1],
    rno[2]: marks[2],
    rno[3]: marks[3],
}

print(d)
