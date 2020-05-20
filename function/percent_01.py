import math
# this will check if the profit has 'percent' in it or not...
loop = True
while loop:
    profit = input("How much profit do you want to make? ")
    if profit == "":
        sure_1 = input("Are you sure u don't want to make any profit? ")
        if sure_1.lower() == "yes":
            profit = 0
            break
        else:
            continue
            break
    elif profit[:-2].isdigit() and profit[-1] == "%":
        del profit[-1]
        percent = True
        break
    else:
        break

print(profit)
