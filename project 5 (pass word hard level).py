# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:34:29 2020

@author: arjun
"""

#Password Generator Project hard level
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for l in range(1,nr_letters+1):
  password+=random.choice(letters)
for n in range(1,nr_symbols+1):
  password+=random.choice(numbers)
for s in range(1,nr_symbols+1):
  password+=random.choice(symbols)
#print(password)
random.shuffle(password) 
ram=""
for r in password:
  ram+=r
print(ram)   

  


