# Imports go here
import math
from function.function_01_v2 import not_blank
# Main routine goes here
name = not_blank("This response can not be blank or contain number", "Name: ", True)
print("Hello " + name)
print("Items to sell('xxx' to exit): ")
# set up the items list
items = {}
items_cost = {}
# set up a loop
loop = True
while loop:
    # set up an exit code called "xxx"
    response = not_blank("the item can't be blank or contain number", "Items: ", True)
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
            # Error = Complain
            print("Please enter a number value. ")
            continue
sum_1 = 0
sum_1 = float(sum_1)
print("Please enter the cost for each item (in dollar), and enter 'xxx' to exit ")
for i in items:
    loop = True
    while loop:
        try:
            cost = float(input("Cost for each " + i + ": "))
            items_cost[i] = cost
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
        if len(fixed_cost) == 0:
            sure = not_blank("Please answer this question","Are you sure you don't have any fixed cost? ", True)
            if sure.lower() == "yes":
                break
            else:
                continue
        else:
            break
    else:
        while loop:
            try:
                price = float(not_blank("Please enter a number value", "Please tell us the price for " + fixed, False))
                sum_2 += price
                fixed_cost[fixed] = price
                break
            except ValueError:
                print("Please enter a number value only")

sum_3 = float(sum_1 + sum_2)
print(sum_3)
# this will check if the profit has 'percent' in it or not...
loop = True
while loop:
    question = input("How much profit do you want to make? ")
    if question == "":
        sure_1 = input("Are you sure u don't want to make any profit? ")
        if sure_1.lower() == "yes":
            profit = 0
            break
        else:
            continue
            break
    elif question[:-1].isdigit() and question[-1] == "%":
        percent = True
        profit = question[:-1]
        break
    elif question.isdigit():
        percent = False
        profit = question
        break
    else:
        print("Please enter a valid answer")
        continue
if percent:
    profit = float(profit)
    profit /= 100
    total_cost = sum_3 + sum_3*profit
    print(profit)
    print(total_cost)
    for i in items:
        stuff = items_cost.get(i)
        stuff = float(stuff)
        stuff += stuff * profit
        items_cost[i] = stuff
else:
    profit = float(profit)
    total_cost = profit + sum_3
    print(profit)
    print(total_cost)
    for i in items:
        stuff = items_cost.get(i)
        stuff = float(stuff)
        stuff += profit
        items_cost[i] = stuff
print(items)
print(items_cost)
























