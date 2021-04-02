n = input("ENTER ANY NUMBER\n=> ")
rev_n = n[::-1]

if rev_n[0] == "4":
  print("Ends with 4")
elif rev_n[0] == "8":
  print("Ends with 8")
else:
  print("Ends with neither 4 nor 8")
