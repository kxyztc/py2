# Day 1.1
# print("hey")

# Day 1.2
# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the + sign.")
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")

# Day 1.3
# name = input("what is your name?")
# print(len(name))
# print(type(name))
# new_name = str(name)
# print(len(name))

# two_digit_number = input("Type a two digit number: ")
# int(two_digit_number[1])+int(two_digit_number[2])   

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# height1 = float(height)
# height2 = float(weight)
# Calculate = int(height2 / (height1 ** 2))
# print("Your Body Mass Index is:", Calculate)

# age = input("What is your current age?")
# age_int = int(age)
# remain = 90 - age_int
# x = remain * 365
# y= remain * 52  
# z = remain * 12
# print(f"You have {x} days, {y} weeks, and {z} months left.")

# print("Welcome to the tip calculator!")
# bill = input("What was the total bill? $")
# tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
# people = input("How many people to split the bill? ")
# total_bill = float(bill) + (float(bill) * (float(tip)/100))
# each = round(total_bill / int(people),2)
# print(f"Each person should pay: ${each}")

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0
# # print("This is an even number")
# else
# print("It is not an even number")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
#     if add_pepperoni== "Y":
#         bill += 2
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             bill == bill
#     elif add_pepperoni=="N":
#         bill == bill
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             bill == bill
# elif size == "M":
#     bill += 20
#     if add_pepperoni== "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1 
#         elif extra_cheese == "N":
#             bill == bill
#     elif add_pepperoni=="N":
#         bill == bill
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             bill == bill
# elif size == "L":
#     bill += 25
#     if add_pepperoni== "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             bill == bill
#     elif add_pepperoni=="N":
#         bill == bill
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             bill == bill
# print("Your bill is $"),     print(bill)
# import random
# randominteger = random.randint(1,100)
# print(randominteger)
# if randominteger < 50"
# print("Yur number is small")
# elif randominteger > 50
# print("number big!!")
# elif randominteger == 50
# print("sdfergthju")

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

import random
import time
UserChoice = int(input("Please choose 0 for Rock, 1 for Paper, or 2 for Scissors"))
CmpChoice = random.randint(0,2)
if UserChoice <= 2 and UserChoice >= 0:
    print("Starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!!")
    time.sleep(0.5)
    if UserChoice < CmpChoice:
        if UserChoice == 0:
            print(rock)
        elif UserChoice == 1:
            print(paper)
        else:
            print(scissors)
        time.sleep(1)
        print("You lose!")
    elif UserChoice == CmpChoice:
        if UserChoice == 0:
            print(rock)
        elif UserChoice == 1:
            print(paper)
        else:
            print(scissors)
        time.sleep(1)
        print("its a tie!")
    else:
        if UserChoice == 0:
            print(rock)
        elif UserChoice == 1:
            print(paper)
        else:
            print(scissors)
        time.sleep(1)
        print("You win!")
else:
    print("Invalid Option.")
    UserChoice = int(input("Please choose 0 for Rock, 1 for Paper, or 2 for Scissors"))
    if UserChoice <= 2 and UserChoice >= 0:
        print("Starting in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("GO!!")
        time.sleep(0.5)
        if UserChoice < CmpChoice:
            if UserChoice == 0:
                print(rock)
            elif UserChoice == 1:
                print(paper)
            else:
                print(scissors)
            time.sleep(1)
            print("You lose!")
        elif UserChoice == CmpChoice:
            if UserChoice == 0:
                print(rock)
            elif UserChoice == 1:
               print(paper)
            else:
                print(scissors)
            time.sleep(1)
            print("its a tie!")
        else:
            if UserChoice == 0:
                print(rock)
            elif UserChoice == 1:
                print(paper)
            else:
                print(scissors)
            time.sleep(1)
            print("You win!")
    else:
        print("Invalid Option.")


