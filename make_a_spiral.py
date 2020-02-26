"""
Make a spiral
https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

Name: May Wang
Date: 26-Feb-2020
"""
def spiralize(size):
    # min(size) = 5
    if(size >= 5):
        spiral = []
        num_ones = []
        for i in range(size):
            spiral.append([])
            # Create all zeros
            for j in range(size):
                spiral[i].append(0)
            # Define number of ones in each directional instruction
            if(i <= 2):
                num_ones.append(size)
            else:
                if(i%2 == 1):
                    num_ones.append(size-i+1)
                else:
                    num_ones.append(size-i+2)
        
        x_end = -1
        j = 0
        # Make spiral
        for instr in range(len(num_ones)):
            # Direction: x+, x- (fixed i, change j)
            if(instr%2 == 0):  
                y_start = j
                # Direction 1: x+ (j++)
                if(instr%4 == 0):
                    i = x_end+1
                    step = 1
                    y_end = y_start+num_ones[instr]
                # Direction 2: x- (j--)
                else:
                    i = x_end-1
                    step = -1
                    y_end = y_start-num_ones[instr]
                # Add ones
                for j in range(y_start,y_end,step):
                    spiral[i][j] = 1
            # Direction: y+, y- (change i, fixed j)
            else:
                x_start = i
                # Direction 3: y+ (i++)
                if(instr%4 == 1):
                    j = y_end-1
                    step = 1
                    x_end = x_start+num_ones[instr]
                # Direction 4: y- (i--)
                else:
                    j = y_end+1
                    step = -1
                    x_end = x_start-num_ones[instr]
                # Add ones
                for i in range(x_start,x_end,step):
                    spiral[i][j] = 1
    
    return spiral

#Test.assert_equals(spiralize(5), [[1,1,1,1,1],
#                                  [0,0,0,0,1],
#                                  [1,1,1,0,1],
#                                  [1,0,0,0,1],
#                                  [1,1,1,1,1]])
#Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
#                                  [0,0,0,0,0,0,0,1],
#                                  [1,1,1,1,1,1,0,1],
#                                  [1,0,0,0,0,1,0,1],
#                                  [1,0,1,0,0,1,0,1],
#                                  [1,0,1,1,1,1,0,1],
#                                  [1,0,0,0,0,0,0,1],
#                                  [1,1,1,1,1,1,1,1]])

print(spiralize(5))
print(spiralize(8))
