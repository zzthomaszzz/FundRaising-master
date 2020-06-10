# check if the name is not blank
'''def not_blank(error, question, no_num):
    # set up a loop...
    loop = True
    while loop:
        response = input(question)
        has_errors = ""
        # check to see if response can contain number or not...
        if no_num:
            for letter in response:
                if letter.isdigit():
                    has_errors = 'yes'
                    break
        # if response is blank...
        if __name__ == '__main__':
            if response == "":
                print(error)
                continue
            # if response has number or not...
            elif has_errors != "":
                print(error)
                continue
            # response can be anything...
            else:
                return response'''


def not_blank(error, subject, num):
    loop = True
    while loop:
        fail = False
        response = input(subject)
        if response == "":
            print(error)
            continue
        else:
            if not num:
                for letter in response:
                    if letter.isdigit():
                        fail = True
                if fail:
                    print(error)
                    continue
                else:
                    return response
            else:
                return response


def num_check(error, subject):
    loop = True
    while loop:
        fail = False
        ask = not_blank(error, subject, True)
        for letter in ask:
            if not letter.isdigit():
                fail = True
        if fail:
            print(error)
            continue
        else:
            return ask
shopping = []


def get_items(heading, item, price):
    print(heading)
    loop = True
    while loop:
        item_list = []
        item_name = not_blank("Please enter a name", item, False)
        if item_name.lower() == "xxx":
            if len(shopping) > 1:
                break
            else:
                print("Please enter at least one item")
                continue
        else:
            item_price = num_check("Please enter a price", price)

        item_list.append(item_name)
        item_list.append(item_price)
        shopping.append(item_list)

    return shopping


stuff = get_items("Variable cost", "Item: ", "Price: ")
print(stuff)


