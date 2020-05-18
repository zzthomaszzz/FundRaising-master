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

name = not_blank("This response can not be blank or contain number", "What is your name? ", True)
print(name)






