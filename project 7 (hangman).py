# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:04:54 2020

@author: arjun
"""
import random
word_list = ["car","bus,","truck","bike","bycycle"]
choose_word = random.choice(word_list)
#print(f"trail test the code {choose_word}")
len_word = len(choose_word)
display =[]
for i in range (len_word):
  display+="_"
end_game = False  
lives = 6

while not end_game:
  guess_letter =input("enter the letter: ")
  if guess_letter in display:
      print(f"you are already guess this letter {guess_letter}")
  for l in range(len_word):
    letter = choose_word[l]
    if guess_letter == letter:
      display[l]=letter
      print(f"you chosen the right letter {guess_letter}")
  if guess_letter not in choose_word:
    lives-=1
    print(f"you chosen wrong letter {guess_letter}")
    print(f"you lives is know {lives}")
    if lives==0:
      end_game=True
      print("you lose better luck next time")
  print(display)  
  if "_"not in display:
    end_game=True 
    print("you won the game") 
  

    

    
