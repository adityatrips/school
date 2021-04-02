def add2dict(d, k, v):
  d[k] = v


running = True
d = {}

while running:
  team_name = input("ENTER THE TEAM NAME\n=> ")
  team_wins = int(input("ENTER THE NUMBER OF MATCHES THE TEAM WON\n=> "))
  team_lost = int(input("ENTER THE NUMBER OF MATCHES THE TEAM LOST\n=> "))
  team_stat = [team_wins, team_lost]
  add2dict(d, team_name, team_stat)
  q = input(
      "QUIT ENTERING AND PRINT STAT or PRINT DICTIONARY AND CONTINUE ADDING (q/p)\n=> "
  ).lower()
  if q == 'q':
    running = False
  else:
    print(d)

print("1: ENTER A TEAM NAME AND GET THE WINNING PERCENT")
print("2: NUMBER OF WINS OF EACH TEAM")
print("3: PRINT TEAM WITH WINNING RECORDS")
dec = int(input("ENTER A CHOICE\n=> "))
if dec == 1:
  t_name = input("ENTER THE TEAM NAME\n=> ")
  for key, val in d.items():
    if key == t_name:
      win_percent = val[0] / (val[0]+val[1])
      print(f"WIN PERCENT = {win_percent}")

elif dec == 2:
  for key, val in d.items():
    print(f'NUMBER OF WINS {key} HAS IS {val[0]}')
elif dec == 3:
  win_rec = []
  for key, val in d.items():
    if val[0] > val[1]:
      win_rec.append(key)
  print(f"{' '.join(win_rec)} HAVE WINNING RECORDS")
else:
  print("INVALID CHOICE")
