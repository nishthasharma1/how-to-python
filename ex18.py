#functions: 1. name piece of code the way variables name strings and numbers
#2: take arguments the way your scripts take argv
#3. using 1 + 2, they let you make mini scripts or tiny commands

#this function is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}")

#this one takes no arguments 
def print_none(): 
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

'''
def means define


'''