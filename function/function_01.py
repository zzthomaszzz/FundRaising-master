# Functions goes in here


def not_blank(error, question, no_num):

    loop = True
    while loop:
        response = input(question)
        if response == "":
            print(error)
            continue
        else:
            if not no_num:
                return response
            else:
                for i in response:
                    if i.isdigit():
                        fail = True
                        break
                if fail:
                    print(error)
                    break
                else:
                    return response


def blank_check(subject):
    loop = True
    while loop:
        check = input(subject)
        if check == "":
            print("This can't be blank")
            continue
        else:
            return check


def num_check(subject):
    for i in subject:
        if not i.isdigit():
            return False
        else:
            return True


def no_num_check(subject):
    for i in subject:
        if i.isdigit():
            return False
        else:
            return True


def yes_number(subject):
    loop = True
    while loop:
        check = blank_check(subject)
        valid = num_check(check)
        if valid:
            break
        else:
            print("Please enter number only")
            continue


def no_number(subject):
    loop = True
    while loop:
        check = blank_check(subject)
        valid = no_num_check(check)
        if valid:
            break
        else:
            print("Please enter words only")
            continue


no_number("Testing: ")