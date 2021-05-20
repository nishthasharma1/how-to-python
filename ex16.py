from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"""
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
""")

input ("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() 

'''
study drills: 
1. 
line 1: importing features/modules 
line 3: assigning the script
line 5,6,7: printing directions
line 9: inputting values

2. i can make it shorter with 1 line

3. 

'''