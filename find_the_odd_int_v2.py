"""
Find the odd int (v2)
Date: 07-Feb-2020
"""
def find_it(seq):
    for n in seq:
        if(seq.count(n)%2 == 1):
            return n