"""
Square Every Digit
Date: 07-Feb-2020
"""
def square_digits(num):
    num_str = str(num)
    out_str = ''
    for n in range(len(num_str)):
        out_str = out_str + str(int(num_str[n])**2)
    return int(out_str)
