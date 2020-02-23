"""
Replace With Alphabet Position
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

Name: May Wang
Date: 23-Feb-2020
"""
def alphabet_position(text):
    # Import alphabet list
    import string
    alphabet_list = list(string.ascii_lowercase)
    
    # text in lowercase
    text_low = list(text.lower())
    
    # Alphabet position (str) in list
    alphabet_pos_list = []
    for i in range(len(text)):
        if(text_low[i] in alphabet_list):
            alphabet_pos_list.append(str(alphabet_list.index(text_low[i])+1))    
    
    # Alphabet position in string
    alphabet_pos = ""
    for i in range(len(alphabet_pos_list)):
        alphabet_pos += alphabet_pos_list[i]
        if(i < len(alphabet_pos_list)-1):
            alphabet_pos += " "

    return alphabet_pos

#from random import randint
#test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
#test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
#
#number_test = ""
#for item in range(10):
#    number_test += str(randint(1, 9))
#test.assert_equals(alphabet_position(number_test), "")

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

from random import randint
number_test = ""
for item in range(10):
    number_test += str(randint(1, 9))
print(alphabet_position(number_test))