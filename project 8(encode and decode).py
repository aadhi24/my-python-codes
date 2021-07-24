# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:49:20 2020

@author: arjun
"""


#from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nest = True
#print(logo)
while nest:
    code=input("decode or encode \n")
    text = input("enter the word \n ")
    shift= int(input("enter the shift key \n "))
    
    def encrypt(words,key,decode):
      
      encode=""
      if "encode" in decode:
        for letter in words:
          if letter in alphabet:
            position = alphabet.index(letter)
            new_key=position+key
            new_word=alphabet[new_key]
            encode+=new_word
          else:
            encode+=letter
        print(f"Your encoded result is : {encode}")
      elif "decode" in decode: 
          for letter in words:
            if letter in alphabet: 
              position = alphabet.index(letter)
              new_key=position-key
              new_word=alphabet[new_key]
              encode+=new_word
            else:
              encode+=letter  
          print(f"Your decoded result is : {encode}")  
      else:
          print("you type the wrong option")
                
           
          
    shift=shift%26      
    encrypt(words=text,key=shift,decode=code) 
    continues=input("Do you want to continue 'yes' or 'no' \n") 
    if "yes" in continues:
      nest=True
    elif "no" in continues:
      nest=False 
      print("bye") 