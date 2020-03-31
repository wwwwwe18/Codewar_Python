"""
The observed PIN
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

Name: May Wang
Date: 31-Mar-2020
"""
# 1 2 3
# 4 5 6
# 7 8 9
#   0

# Rule:
# - It is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally).
# - You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

def get_pins(observed):
    # Save key and its adjacent into list
    key_list = [['0','8','','',''],['1','2','4','',''],['2','1','3','5',''],['3','2','6','',''],['4','1','5','7',''],['5','2','4','6','8'],['6','3','5','9',''],['7','4','8','',''],['8','5','7','9','0'],['9','6','8','','']]
    
    # Generate temp PIN list
    pin_list = []
    for i in range(5**len(observed)):
        pin_list.append("")
    for i in range(len(observed)):
        count = 0
        for j in range(0,5**(len(observed)-1-i)):
                for k in range(0,5):
                    for z in range(0,5**i):
                        pin_list[count] += str(key_list[int(observed[i])][k])                
                        count += 1
    
    # Generate output PIN list
    out = []
    for i in range(5**len(observed)):
        if(len(pin_list[i]) == len(observed)):
            out.append(pin_list[i])
    out = sorted(out)
    
    return out

#test.describe('example tests')
#expectations = [('8', ['5','7','8','9','0']),
#                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
#                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]
#
#for tup in expectations:
#  test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])

expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

for tup in expectations:
    print(get_pins(tup[0]))
    print(sorted(tup[1]))
    print("")

# Additional tests
