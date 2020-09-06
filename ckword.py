#!/usr/bin/env python
import getopt
import sys
import re


listOfStrings = []
def my_function(input_string, input_c, level):
#    print("input_string: ",input_string)
#    print("input_char:",input_c)
#    print("level ", level)
    if level > 1:
        input_string = input_string[1:level]
        level = level - 1
        word = input_string[0]
        for fc in range(0, len(word)):
#            print("B input_string :", input_string)
            s_in = input_c + word[fc]
            my_function(input_string, s_in, level)

    else:
        if is_word(input_c):
            if input_c not in listOfStrings:
                listOfStrings.append(input_c)
                print(input_c)

def is_word(word):
        return word.lower() in words

file = open("/usr/share/dict/words", "r")
words = re.sub("[^\w]", " ",  file.read()).split()

#test_string = "peripheral h l"
input_string = sys.argv[1] 

string_sp = input_string.split()
t_count = len(string_sp)
word = string_sp[0]
for fcc in range(0, len(word)):
    my_function(string_sp, word[fcc], t_count)
