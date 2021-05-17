formatter = "{} {} {} {}" #placeholders

print(formatter.format(1,2,3,4)) #formats to add 1,2,3,4 into the line
print(formatter.format("one","two","three","four")) #formats one, two, three, four
print(formatter.format(True, False, False, True)) #formats an addition of true, false, false, true
print(formatter.format(formatter, formatter, formatter, formatter)) #prints the variable 'formatter' 4 times
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) #prints the poem

