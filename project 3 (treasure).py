print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
enter =input("Do you want to enter game yes or no? ").lower()
if enter== "yes":
  print("your in the forest know")
  way = input("Your are in the junction of the forest which way to go left or right ").lower()
  if way =="left":
    print("know your are near the river ")
    print("if you wait for a minute the boat will come to you or you can swim across to the island ")
    boat = input("option are boat or swim ").lower()
    if boat=="boat":
      print("your arrived in the island their is a old house with 3 door ")
      door =input("option for door their are 3 colour yellow,green,white? ").lower()
      if door == "white":
        print("you got the treasure (winner)")
      elif door == "green":
        print("your in the fire ")
        print("game over")
      elif door =="yellow":
        print("your are killed by jason ")
        print("game over")
      else:
        print("maker sure you take the right option")
    elif boat =="swim":
      print("your attacked by a piranha")
      print("game over")
    else:
      print("your option not the game")
  elif way =="right":
    print("the way is end ")
    print("game over")
  else:
    print("this option is not available")
else:
  print("go away ")
