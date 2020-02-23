"""
Find the missing letter
https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

Name: May Wang
Date: 23-Feb-2020
"""
def find_missing_letter(chars):   
    # Import alphabet list
    import string
    alphabet_list = list(string.ascii_lowercase)

    if(len(chars) >= 2):
        # Find the first elem in alphabet list
        first_elem = alphabet_list.index(chars[0].lower())
        
        # Compare the chars with alphabet list
        for i in range(len(chars)):
            if(chars[i].lower() != alphabet_list[first_elem]):
                missing_letter = alphabet_list[first_elem]
                break
            else:
                first_elem += 1

    # Output lowercase/uppercase
    if(chars[0].isupper() == True):
        missing_letter = missing_letter.upper()
    
    return missing_letter

#test.describe("kata tests")
#test.it("example tests")
#test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
#test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')

print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))