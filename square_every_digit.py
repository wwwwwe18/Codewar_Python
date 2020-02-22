"""
Square every digit
https://www.codewars.com/kata/546e2562b03326a88e000020

Name: May Wang
Date: 07-Feb-2020
"""
def square_digits(num):
    num_str = str(num)
    out_str = ''
    for n in range(len(num_str)):
        out_str = out_str + str(int(num_str[n])**2)
    return int(out_str)

#test.assert_equals(square_digits(9119), 811181)

print(square_digits(9119))
