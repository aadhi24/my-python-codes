# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:22:12 2021

@author: arjun
"""

from art import logo, vs
from game_data import data
from replit import clear
import random


# create a fuction call the random
def get_random():
    return random.choice(data)


# need a fuction to access the dictionary key and value
def fuction_dic(account_a, account_b):
    print(logo)
    name = account_a['name']
    description = account_a['description']
    country = account_a['country']
    print(f"Compare A: {name}, {description} , {country}.")
    print(vs)
    name = account_b['name']
    description = account_b['description']
    country = account_b['country']
    print(f"Against B: {name}, {description} , {country}.")


# make function for compare
def compare(option, followers_a, followers_b):
    if followers_a > followers_b:
        return option == "a"
    else:
        return option == "b"


score = 0
game_should_continue = True
account_a = get_random()
account_b = get_random()

# need to make a while loop
while game_should_continue:
    fuction_dic(account_a, account_b)
    # need to create input "a" or "b"
    option = input("Who has more followers? Type 'A' or 'B': ")
    account_a = account_b
    account_b = get_random()
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    correct = compare(option, followers_a, followers_b)
    clear()
    if correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f" your score {score}")
