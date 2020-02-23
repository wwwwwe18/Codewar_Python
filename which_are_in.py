"""
Which are in?
https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

Name: May Wang
Date: 23-Feb-2020
"""
def in_array(array1, array2):
    array_out = []
    
    # Calculate the length of each elems
    for a1_elem in array1:
        for a2_elem in array2:
            # Find the substring only len(a1_elem) <= len(a1_elem)
            if(len(a1_elem) <= len(a2_elem)): 
                i = 0              
                while(i < len(a2_elem)):
                    if(a1_elem == a2_elem[i:i+len(a1_elem)]):
                        # Ignore the repeat a1_elem
                        if((a1_elem in array_out) == False):
                            array_out.append(a1_elem)
                        break
                    else:
                        i += 1
    # Sort array_out in lexicographical order        
    array_out.sort()
    
    return array_out

#a1 = ["live", "arp", "strong"] 
#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#r = ['arp', 'live', 'strong']
#test.assert_equals(in_array(a1, a2), r)

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))

# Additional tests
a1 = ["1028", "1295", "ar"] 
a2 = ["01028001295", "102800", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))