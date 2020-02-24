"""
The Hashtag Generator
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

Name: May Wang
Date: 24-Feb-2020
"""
def generate_hashtag(s):
    # Add " " at the end of s
    s_tmp = s+" "
    
    out = False
    
    # 0 < len(s) <= 140
    if(len(s) > 0) and (len(s) <= 140):
        # Hashtag at the beginning
        out = "#"
        
        # Remove space and uppercase the first letter
        i = 0
        while(i < len(s_tmp)-1):
            j = i
            while(s_tmp[j] != " "):
                j += 1
            
            # Case0 : the first elem is space
            # Case1 : others
            if(j > 0):
                out += s_tmp[i].upper()+s_tmp[i+1:j].lower()
            i = j+1
            
            # Deal with multiple spaces
            while(i < len(s_tmp)) and (s_tmp[i] == " "):
                i += 1
    
    return out

#Test.describe("Basic tests")
#Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
#Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
#Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
#Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
#Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
#Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
#Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
#Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
#Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
#Test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')

print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag')[0])
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))

# Additional tests
# Output: #CvpbbrurRbLmlxfjvnjzxBWekmgwrHfxxxkbovlwSvpuenugjmg
print(generate_hashtag('CvpBBRuR rB LMLxfJvNJzX b WEkMgWr   HfxxXKBovlW SVPuenUGJmg'))

# Output: #VajvnGexqUuzumvsvdcmZtdratsiexzMydbdyrtrelLfqnblbyarvSdxlkqmugth
print(generate_hashtag('VaJvN geXQ uuzUmVSvDcm ztDRATsIeXz mydbdYrtREL LfqNbLByARv sDxLKqMuGTH'))
    
# Output: #Fkbfzqzrkb
print(generate_hashtag(' fKBFZqZrKB'))