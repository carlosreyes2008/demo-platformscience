def BooleanInput(msg):
    result = None

    while result == None:
        print(f"{msg} [y/n]")
        answer = input()

        if answer == "y":
            result = True
        elif answer == "n":
            result = False
        else:
            print("Invalid input. Please, just use 'y' or 'n'")
    
    return result