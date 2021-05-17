tabby_cat = "\tI'm tabbed in." #the \t adds a tab before the string
persian_cat = "I'm split\non a line." #the \non takes out the word after it
backlash_cat = "I'm \\ a \\ cat." #the \\ takes away one \ and surrounds a with \ on each side

fat_cat = '''
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
'''
# the """ also include # within them
#the \t added a tab and the * was like a bullet point
print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

#how do i combine escape qequences (\) and format strings to create a more complex format?? 