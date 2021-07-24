import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
you_won='''

██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝'''


you_lose='''
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗████████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░░░░██║░░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗░░░██║░░░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝░░░██║░░░
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░░░░╚═╝░░░
'''
draw ='''

██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
██║░░██║██╔══██╗██╔══██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░
'''

choose = int(input("what is your choose ? Type 0 for rock ,1 for paper or 2 for scissors\n "))
if choose>=0 and choose<=2:
   #my chooose
  items =[rock,paper,scissors]
  my =items[choose]
  print("your choose")
  print(my)
  print("machine choose")
  #machine choose
  pc_choose= random.randint(0,2)
  machine =items[pc_choose] 
  print(machine)
  

  if pc_choose==0 and choose==2:
    print(you_lose)
    print("computer wins")
  elif pc_choose==1 and choose==0:
    print(you_lose) 
    print("computer wins")
  elif pc_choose==2 and choose==1:
    print(you_lose) 
    print("computer wins")
  elif choose==0 and pc_choose==2:
    print(you_won)  
  elif choose==1 and pc_choose==0:
    print(you_won)  
  elif choose==2 and pc_choose==1:
    print(you_won)
  else:
    print(draw)
else:
  print("get out")






