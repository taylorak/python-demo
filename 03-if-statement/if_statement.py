'''
Working with if-then statements
'''


def if_else(correct):
    "Checks if correct is true or not"
    if correct:
        print("true statement")
    else:
        print("false statement")

if_else(True)
if_else(False)


def check_nums(num1, num2):
    '''
    Checks which number is greater
    '''
    if num1 > num2:
        print("{} is greater than {}".format(num1, num2))
    elif num2 > num1:
        print("{} is greater than {}".format(num2, num1))
    else:
        print("{} is equal to {}".format(num1, num2))

check_nums(1, 2)
check_nums(2, 1)
check_nums(2, 2)


def ternary_if(correct):
    "Checks if correct is true or not"
    statement = "true statment" if correct else "false statment"
    print(statement)

ternary_if(True)
ternary_if(False)
