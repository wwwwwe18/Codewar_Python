"""
You're a square!
https://www.codewars.com/kata/54c27a33fb7da0db0100040e

Name: May Wang
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

#test.describe("is_square")
#test.it("should work for some examples")
#test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
#test.assert_equals(is_square( 0), True, "0 is a square number")
#test.assert_equals(is_square( 3), False, "3 is not a square number")
#test.assert_equals(is_square( 4), True, "4 is a square number")
#test.assert_equals(is_square(25), True, "25 is a square number")
#test.assert_equals(is_square(26), False, "26 is not a square number")

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))