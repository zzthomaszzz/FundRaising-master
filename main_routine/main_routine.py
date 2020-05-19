# Imports go here
import math
from function.function_01_v2 import not_blank
# Main routine goes here
name = not_blank("This response can not be blank or contain number", "What is your name? ", True)
print("Hi " + name)
print("Please enter items that you would like to sell, if you would like to stop, please enter 'xxx'T")
# set up the items list
items = {}
# set up a loop
loop = True
while loop:
    # set up an exit code called "xxx"
    response = not_blank("this cant be blank", "Items: ", False)
    # check to see if the number of items is more than 0...
    if response == 'xxx':
        if len(items) > 0:
            break
        else:
            print("Please add at least one item. ")
            continue
    # add items to the list but with the "None" value since they have not gotten any quantities...
    else:
        items[response] = 'none'
print("Please enter the quantity for items that you have chosen to sell")
# for every item, the program will ask for the quantity...
for i in items:
    # Loop - literal loop.
    loop = True
    while loop:
        number = input("Quantity for " + i + ": ")
        # check to see if the quantity is a number (Integer)
        if number.isdigit():
            items[i] = number
            # Break the loop since we have got the quantity of the item
            break
        else:
            # Error = Complain!
            print("Please enter a number value. ")
            continue
sum_1 = 0
sum_1 = float(sum_1)
print("Please enter the cost for each item (in dollar)")
for i in items:
    loop = True
    while loop:
        cost = float(input("what is the cost for each " + i + " ? "))
        try:
            cost = float(cost)
            # cost_2 = variable that is the item in the items dictionary)
            cost_2 = items.get(i)
            # convert cost_2 to float so we can do some math with it...)
            cost_2 = float(cost_2)
            # cost_1 = the cost for the items with the quantity of its...)
            cost_1 = float(cost * cost_2)
            # sum_1  sub-total cost after the loop actually ended
            sum_1 += cost_1
            break
        except ValueError:
            print("Please enter a value in dollar.")
print("here is the sub-total cost for your items (in dollars): ")
print(sum_1)
# This below will get the fixed-cost...
fixed_cost = {}
sum_2 = 0
sum_2 = float(sum_2)
print("Please tell us your fixed-costs, and enter 'xxx' to exit ")
loop = True
while loop:
    fixed =(not_blank("Please enter a name ", "fixed-cost: ", True))
    if fixed == "xxx":
        if len(fixed) == 0:
            sure = not_blank("This can't be blank", "Are you sure you do not have any fixed-cost? ", False)
            if sure.lower() == "yes":
                break
            else:
                continue
        else:
            break
    else:
        try:
            price = float(not_blank("Please enter a number value", "Please tell us the price for " + fixed, False))
            sum_2 += price
            fixed_cost[fixed] = price
        except ValueError:
            print("Please enter a number value only")
sum_3 = float(sum_1 + sum_2)
print(sum_3)
print("what is the profit you want to make")
profit = input()

















