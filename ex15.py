#from sys import argv #used argv to get filename ->

#script, filename = argv 

#txt = open(filename) #actually open the file

#print(f"Here's your file {filename}:")
#print(txt.read())

print("Type the filename again:")
file_again = input ("> ")

txt_again = open(file_again)

print(txt_again.read())