"""
Who likes it?
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

Name: May Wang
Date: 05-Feb-2020
"""
def likes(names):
    num_likes = len(names)
    #your code here
    if(num_likes == 0):
        print("no one likes this")
    elif(num_likes == 1):
        print(names[0] + " likes this")
    elif(num_likes == 2):
        print(names[0] + " and " + names[1] + " like this")
    elif(num_likes == 3):
        print(names[0] + ", " + names[1] + " and " + names[2] + " like this")
    else:
        print(names[0] + ", " + names[1] + " and " + str(num_likes-2) + " others like this")

#Test.assert_equals(likes([]), 'no one likes this')
#Test.assert_equals(likes(['Peter']), 'Peter likes this')
#Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

likes([])
likes(['Peter'])
likes(['Jacob', 'Alex'])
likes(['Max', 'John', 'Mark'])
likes(['Alex', 'Jacob', 'Mark', 'Max'])