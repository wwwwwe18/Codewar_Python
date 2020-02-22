"""
Take a Ten Minute Walk
https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

Name: May Wang
Date: 22-Feb-2020
"""
def is_valid_walk(walk):
    #determine if walk is valid
    out = False
    
    if(len(walk) == 10):
        count_x = 0
        count_y = 0 
        for i in range(10):
            if(walk[i] == 'n'):
                count_y += 1
            if(walk[i] == 's'):
                count_y -= 1
            if(walk[i] == 'e'):
                count_x += 1
            if(walk[i] == 'w'):
                count_x -= 1
        if(count_x == 0) and (count_y == 0):
            out = True
    return out

#some test cases for you...
#test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
#test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
#test.expect(not is_valid_walk(['w']), 'should return False');
#test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(not is_valid_walk(['w']))
print(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))