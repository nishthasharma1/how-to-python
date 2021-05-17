types_of_people = 10 #the 'types of people
x = f"There are {types_of_people} types of people." #explanation to the reader

binary = "binary" #either or statement
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x) #writing it on
print(y)

print(f"I said: '{x}''")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)