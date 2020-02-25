"""
Range Extraction
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

Name: May Wang
Date: 25-Feb-2020
"""
def solution(args):
    out_tmp = ""
    
    i = 0
    while(i < len(args)):
        # Record the first elem
        start = i
        j = i+1
        while(j < len(args)):
            # Find the continuous elem
            if(args[j] == args[i]+1):
                i += 1
                j += 1
            else:
                break
        
        #print(start)
        #print(i)
        #print(j)
        #print(args[start:j])
        
        # Consider a range if it spans at least 3 numbers
        if(j >= start+3):
            out_tmp += str(args[start])+"-"+str(args[j-1])+","
        else:
            for i in range(start,j):
                out_tmp += str(args[i])+","
        i = j
        
        #print(out_tmp)
    
    # Remove the last ","
    out = out_tmp[0:len(out_tmp)-1]
    
    return out

#Test.describe("Sample Test Cases")
#Test.it("Simple Tests")
#Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
#Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
print(solution([-3,-2,-1,2,10,15,16,18,19,20]))