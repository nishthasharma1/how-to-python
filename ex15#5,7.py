from sys import argv 
# #used argv to get filename ->

script, filename = argv 

txt = open(filename) #actually open the file that has the text on it

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input ("> ") #inputting the filename 

txt_again = open(file_again)

print(txt_again.read())


'''
study drills: 

3. commands = functions = methods

5. HUHUUHUHUHUH


'''