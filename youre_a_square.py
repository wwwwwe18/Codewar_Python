"""
You're a square!
Date: 07-Feb-2020
"""
import math
def is_square(n):
    out_bool = False
    if(n == 0):
        out_bool = True
    elif(n > 0):
        if(math.sqrt(n) == int(math.sqrt(n))):
            out_bool = True
    return out_bool