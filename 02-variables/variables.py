'''
Working with data types and variables
'''

# constants
NAME = "Taylor"
AGE = 24

# print(NAME + " is " + str(AGE) + " years old")
# print("{} is {} years old".format(NAME, AGE))


def print_global_age():
    "Prints the global variables NAME and AGE"
    print("{} is {} years old\n".format(NAME, AGE))


def print_parameter_age(name, age):
    "Prints the parameters name and age"
    print("{} is {} years old\n".format(name, age))


def print_local_age():
    "Prints local variables name and age"
    name = "Taylor"
    age = 24
    print("{} is {} years old\n".format(name, age))


print("using global variable:")
print_global_age()

print("using function parameters:")
print_parameter_age(NAME, AGE)

print("using local variable:")
print_local_age()

# variable is out of scope
# print("{} is {} years old\n".format(name, age))
