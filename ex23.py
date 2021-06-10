import sys
script, encoding, error = sys.argv 


def main(language_file, ecoding, errors):
    line = language_file.readline()

    if line: 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors='strict')
    cooked_string = raw_bytes.decode(encoding, errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

'''
code breakdown: 
line 5: start with 'main' function  - called at the end of the script to get things going
6: read one line from the languages file it is given, 'readlines' when dealing with files
8: if statement: testing whether 'line' has something in it, the readline function will return an empty string 
- as long as 'readline'' gives something, it will be true and the code in line9-10 will run
- if false, the python skips line 9-10

9: separate function to print_line - once you know what it does then you can just use that 

10: calling 'main' inside 'main' - which basically makes the function jump to the top and run it again - making a LOOP

11: start the definiton for the print_line fnction, which does actual encoding of each line from language.txt

12. sample stripping of the trailing \n on line string

13. take langauges receieved from langages.txt file and 'encode' it into the raw bytes
- remember DBES: Decode Bytes, Encode Strings
the next_lang variable is a string, so to get raw bytes, you call .encode() on it to "encode strings"
pass to encode() then encoding i want and how to handle the errors

14: the extra step of showing the inverse of line 15 by creating cooked_string varible from the raw_bytes
- remember DBES says Decode Bytes
and raw_bytes is bytes so we called .decode() on it to get a python string - should be same as next_lang variable

15: done defining functions, now the language.txt file opens

16: the end of hte script runs the main funciton with all correct arameters to get everything going and kick start loop
remember this jumps to where the main function is defined on line 5 and on 10, main is called again
causing loop to keep going 
the if line: on line 8 prevent loop from going on forever


'''