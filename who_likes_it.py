"""
Who likes it?
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
