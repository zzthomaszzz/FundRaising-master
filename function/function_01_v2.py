# check if the name is not blank
def not_blank(error, question, no_num):
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
        if response == "":
            print(error)
            continue
        # if response has number or not...
        elif has_errors != "":
            print(error)
            continue
        # response can be anything...
        else:
            return response
