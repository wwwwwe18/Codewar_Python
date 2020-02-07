"""
Find the odd int
Date: 07-Feb-2020
"""
def find_it(seq):
    seq = sorted(seq)
    n = 0
    while(n < len(seq)):
        count1 = n
        while(seq[n] == seq[count1]):
            count1 = count1 + 1
            if(count1 == len(seq)):
                break
        if((count1-n)%2 == 1):
            num_odd = seq[n]
        n = count1
    return num_odd