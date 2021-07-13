#while loops
#they do a test like an if-statement, but they keep jumping to the 'top' where the while is and repeat until the experssion is false

''' 
some rules to give an end to your while-loop: 
1. make sure that they are used sparingly - usually for loops are better
2. review your while statements and make sure that the boolean test will become false at some point
3. when in doubt, print out your test variable at the top and the bottom of hte while-loop to see what it's doing
'''
i = 0
numbers = []

while i < 6: 
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers: 
    print(num)

'''
study drills:
1. ??? 

'''
