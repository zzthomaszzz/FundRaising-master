# Imports go here
from function.function_01 import not_blank
# Main routine goes here
name = not_blank("This response can not be blank or contain number", "What is your name? ", True)
print("Please enter items that you would like to sell, if you would like to stop, please enter 'xxx'T")

items = {}
loop = True
while loop:
    response = not_blank("this cant be blank", "Items: ", False)
    if response == 'xxx':
        if len(items) > 0:
            break
        else:
            print("Please add at least one item. ")
            continue
    else:
        items[response] = 'none'
print("Please enter the quantity for items that you have chosen to sell")
for i in items:
    loop = True
    while loop:
        number = input("Quantity for " + i + ": ")
        if number.isdigit():
            items[i] = number
            break
        else:
            print("Please enter a number value. ")
            continue
sum = 0
print("Please enter the cost for each item (in dollar)")
for i in items:
    loop = True
    while loop:
        cost = input("what is the cost for " + i + " ? ")
        try:
            cost = float(cost)
            cost_2 = items.get(i)
            cost_2 = float(cost_2)
            cost_1 = cost * cost_2
            sum += cost_1
            break
        except ValueError:
            print("Please enter a value in dollar.")
print("here is the sub-total cost for your items")
print("Sub-total cost: " + sum)












