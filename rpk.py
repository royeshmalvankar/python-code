#function for random computer input
from random import randint
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
cm = t[randint(0,2)]
#print(computer_move).   #uncomment the print statement
#print this above code multiple times & observe Output.
d= {
    "Rock":"🗿",
    "Paper":"📃",
    "Scissors":"✂️",
    "exit":"🚪"
}

p1 = ""
w=0
l=0
t=0
p=0
while p1 != "exit":
#set player to user input
  p1 = input("\nEnter the following Input:\n1)Rock \n2)Paper \n3)Scissors \nIf not type 'exit' :")
  print("You selected:",d[p1])
  if p1!="exit":
    print("Computer selected:",d[cm])
    
		#if-else for all 3 above conditions here.
  if p1==cm:
    t+=1
    p+=1
    print("\nTie\nBoth are Brothers")
  elif p1=="Rock" and cm=="Paper":
    l+=1
    p+=1
    print("\nComputer wins with 📃 \nPaper wraps Rock")
  elif p1=="Scissors" and cm=="Rock":
    l+=1
    p+=1
    print("\nComputer Wins with 🗿\nRock smash Scissor")
  elif p1=="Paper" and cm=="Scissors":
    l+=1
    p+=1
    print("\nComputer Wins with ✂️\nScissor cuts Paper")
  elif cm=="Rock" and p1=="Paper":
    w+=1
    p+=1
    print("\nYou win with 📃\nPaper wraps Rock")
  elif cm=="Scissors" and p1=="Rock":
    w+=1
    p+=1
    print("\nYou Win with 🗿\nRock smash Scissor")
  elif cm=="Paper" and p1=="Scissors":
    w+=1
    p+=1
    print("\nYou Win with ✂️\nScissor cuts Paper")
  elif p1=="exit":
    break
  else:
    print("\nWrong Input")
if p1=="exit":
  print("\nTotal Games Played:",p)
  print("\nTotal wins:",w)
  print("Total Losses:",l)
  print("Ties:",t)