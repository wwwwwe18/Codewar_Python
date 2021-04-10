"""
Roman Numerals Encoder
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

Name: May Wang
Date: 10-Apr-2021
"""
# Create a function taking a positive integer as its parameter and
# returning a string containing the Roman Numeral representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately
# starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
#
# Rule
# - 1,2,3  : Remain in level - I,X,C,M
# - 4      : Level up        - V,L,D
# - 5,6,7,8: Remain in level - V,L,D
# - 9      : Level up        - X,C,M
#
# Example
# Org:MCXI
#     MDXI
#     1943
# New:MMLI

def solution(n):
    num_list = [1000,500,100,50,10,5,1]
    sym_list = ['M','D','C','L','X','V','I']

    s_list = []
    n_tmp = n
    for i in range(4):
        s = []
        d = 10**(3-i)
        num = int(n_tmp/d)
        n_tmp = n_tmp%(d)
        
        #print(i)
        #print(d)
        #print(num)
        #print(sym_list[num_list.index(d)])
        
        # 4 or 9 - Level up
        if(num%5==4):
            s.append(sym_list[num_list.index(d)])
            s.append(sym_list[num_list.index(d*5*(round(num/5)))])
        # Others
        else:
            if(num>=5):
                s.append(sym_list[num_list.index(d*5)])
            for j in range(num%5):
                s.append(sym_list[num_list.index(d)])                

        s_list.append(''.join(s))
    
    out_str = ''.join(s_list)
    
    return out_str

#test.assert_equals(solution(1),'I', "solution(1),'I'")
#test.assert_equals(solution(4),'IV', "solution(4),'IV'")
#test.assert_equals(solution(6),'VI', "solution(6),'VI'")
#test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
#test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
#test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
#test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
#test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
#test.assert_equals(solution(1000), 'M', 'solution(1000), M')
#test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
#test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

print(solution(1))
print(solution(4))
print(solution(6))
print(solution(14))
print(solution(21))
print(solution(89))
print(solution(91))
print(solution(984))
print(solution(1000))
print(solution(1889))
print(solution(1989))