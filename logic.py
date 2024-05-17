import random

a="ROCK PAPER SCISSOR"

rock=0
scissor=1
paper=2

choice = int(input("enter the choice 0 -> ROCK 1 -> Scissor 2-> Paper"))

CPU = random.randrange(3)

if(CPU == 0):
  if(choice==0) print('draw')

elif(CPU == 1):
  if(choice==0) print('win')

elif(CPU == 2):
  if(choice==0) print('loss')

else:
  print('enter valid number')
