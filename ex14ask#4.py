from sys import argv

script, user_name, age = argv
prompt = '. ' #what the symbol is in front of input

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

#1: played it, didn't get it haha
#2: it just changes the bullets
#3: did i do this right?? 
#4: print(f""" something something something """")