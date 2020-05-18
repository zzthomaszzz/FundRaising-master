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
                if response.isdigit():
                    print(error)
                    continue
                else:
                    return response






