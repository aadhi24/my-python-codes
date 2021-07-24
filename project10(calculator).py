# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:32:34 2021

@author: arjun
"""

#from art import logo
#print(logo)
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def multi(n1,n2):
  return n1*n2
def division(n1,n2):
  return n1/n2
operation ={
  "+":add,
  "-":sub,
  "*":multi,
  "/":division,
} 
def calucation(): 
  num1 =int(input("enter the first no: "))
  for number in operation:
    print(number)
  loop= True
  while loop:  
    operational=input("the option given above: ")
    num2 =int(input("enter the next no: "))
    dic=operation[operational]
    answer=dic(num1,num2)

    print(f"{num1} {operational} {num2} = {answer}")
    sec_option=input("type 'y' to contin or no 'n'? and to start 's' ")
    if "y" in sec_option:
      num1=answer
    elif "s" in sec_option:
      loop=False
      calucation()
    else:
      loop=False  

calucation()

    
    