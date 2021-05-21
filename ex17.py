from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how? 
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

'''
exists are another command: 
- return true if file exists based on its name ina  string as an argv
- return false if not

** echo to make a file and cat to show the file

study drills:
3. command "con*cat*enates" prints a file to the screen 
- know more through (man cat)

the len() gets the length of the string that you pass to it then returns that as a number

'''