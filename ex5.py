#string is how you make something that your program might give to a human
#format string: everytime you use a "" its a string
#embed variables by using {} and stat with f for format

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exacly right
total = age + height + weight
f = height_in_cm = height * 2.54
round(height_in_cm)
weight_in_kg = weight / 2.2046
round(weight_in_kg)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"In other measurements, he is {f} cm tall and {weight_in_kg} kg.")