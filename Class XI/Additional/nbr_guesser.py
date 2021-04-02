from random import randint
num = randint(10, 50)

for i in range(1, 6):
  guess = int(input("Enter the number in your mind from 10 to 50\n=> "))
  if guess == num:
    print("You won!")
    break
  else:
    print("Try again!")
print(f"Program over! The computer generated number was {num}")
