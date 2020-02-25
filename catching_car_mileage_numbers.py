"""
Catching Car Mileage Numbers
https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python

Name: May Wang
Date: 25-Feb-2020
"""
# Instructions

# Output 2
# Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array
# † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

# Output 1
# a 1 if an interesting number occurs within the next two miles

# Error Checking
# A number is only interesting if it is greater than 99!
# Input will always be an integer greater than 0, and less than 1,000,000,000.
# The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
# You should only ever output 0, 1, or 2.

# Check whether number is interesting: output 0 or 2
def interesting_check(number, awesome_phrases):
    check_rule2 = 0

    check0_rule3 = 0
    check1_rule3 = 0
    location_0 = -1
    location_9 = -1
    
    check_rule4 = 0
    
    interest_check = 0
    
    # Check the extreme case
    if(number < 97) or (number > 1000000002):
        interest_check = 0
    else:
        # Save number as string
        number_str = str(number)
        
        elem0 = number_str[0]
        for i in range(len(number_str)):
            # Interesting number 2: Every digit is the same number: 1111
            if(number_str[i] == elem0):
                check_rule2 += 1
            # Interesting number 3: The digits are sequential, incementing†: 1234  
            if(number_str[i] == str((int(elem0)-i)%10)):
                check0_rule3 += 1
            if(number_str[i] == str((int(elem0)+i)%10)): 
                check1_rule3 += 1
            # Save the location of 0, 9
            if(number_str[i] == "0"):
                location_0 = i
            if(number_str[i] == "9"):
                location_9 = i
        
        # Interesting number 4: The digits are a palindrome: 1221 or 73837
        if(len(number_str)%2 == 0) and (number_str[0:len(number_str)//2] == number_str[len(number_str)-1:len(number_str)//2-1:-1]):
            check_rule4 = 1
        if(len(number_str)%2 == 1) and (number_str[0:len(number_str)//2] == number_str[len(number_str)-1:len(number_str)//2:-1]):
            check_rule4 = 1
        
        # Interesting number 1: Any digit followed by all zeros: 100, 90000
        # Interesting number 5: The digits match one of the values in the awesome_phrases array
        # Interesting number 2, 4
        if(number%100 == 0) or (check_rule2 == len(number_str)) or (check_rule4 == 1) or (number in awesome_phrases):
            interest_check = 2
        # Interesting number 3
        # † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
        # ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
        if(check0_rule3 == len(number_str)) and ((location_0 == -1) or (location_0 == len(number_str)-1)):
            interest_check = 2
        if(check1_rule3 == len(number_str)) and ((location_0 == -1) or (location_0 == location_9+1)):
            interest_check = 2
    
        if((number <= 99) or (number >= 1000000000)) and (interest_check == 2):
            interest_check = 1
    
    return interest_check

# Main define
def is_interesting(number, awesome_phrases):
    # Output 2
    output = interesting_check(number, awesome_phrases)

    # Output 1 if an interesting number occurs within the next two miles
    if(output != 2):
        number_around = [number-2, number-1, number+1, number+2]
        for i in number_around:
            interest_check = interesting_check(i, awesome_phrases)
            if(interest_check == 2):
                output = 1
                break
               
    return output


#test.describe("Basic inputs")
#test.it("should work, dangit!")
#tests = [
#	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
#	{'n': 1336, 'interesting': [1337, 256], 'expected': 1},
#	{'n': 1337, 'interesting': [1337, 256], 'expected': 2},
#	{'n': 11208, 'interesting': [1337, 256], 'expected': 0},
#	{'n': 11209, 'interesting': [1337, 256], 'expected': 1},
#	{'n': 11211, 'interesting': [1337, 256], 'expected': 2},
#]
#for t in tests:
#	test.assert_equals(is_interesting(t['n'], t['interesting']), t['expected'])

tests = [
	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
	{'n': 1336, 'interesting': [1337, 256], 'expected': 1},
	{'n': 1337, 'interesting': [1337, 256], 'expected': 2},
	{'n': 11208, 'interesting': [1337, 256], 'expected': 0},
	{'n': 11209, 'interesting': [1337, 256], 'expected': 1},
	{'n': 11211, 'interesting': [1337, 256], 'expected': 2},
]
for t in tests:
	print(is_interesting(t['n'], t['interesting']))

# Additional tests
print(is_interesting(6666, [1337, 256]))
print(is_interesting(1234, [1337, 256]))
print(is_interesting(7890, [1337, 256]))
print(is_interesting(3210, [1337, 256]))
print(is_interesting(1234, [1337, 256]))
print(is_interesting(1234321, [1337, 256]))
print(is_interesting(1881, [1337, 256]))
print(is_interesting(256, [1337, 256]))
print(is_interesting(987654321, []))
print(is_interesting(654, []))
print(is_interesting(3210, []))
print(is_interesting(67890, []))
print(is_interesting(109, []))
print(is_interesting(1335, [1337, 256]))
print(is_interesting(1339, [1337, 256]))
print(is_interesting(98, [1337, 256]))
print(is_interesting(99, [1337, 256]))
print(is_interesting(1000000001, [1337, 256]))
print(is_interesting(3, [1337, 256]))
print(is_interesting(1, []))