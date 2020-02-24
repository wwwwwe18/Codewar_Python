"""
Moving Zeros To The End
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Name: May Wang
Date: 24-Feb-2020
"""
def move_zeros(array):
    out = []
    
    for i in range(len(array)):
        # int, str: not Zeros
        if(type(array[i]) != bool) and (array[i] != 0):
            out.append(array[i])
        # bool
        if(type(array[i]) == bool):
            out.append(array[i])         

    for i in range(len(out),len(array)):
        out.append(0)
    
    return out

#Test.describe("Basic tests")
#Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
#Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
#Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
#Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
#Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
#Test.assert_equals(move_zeros(["a","b"]),["a","b"])
#Test.assert_equals(move_zeros(["a"]),["a"])
#Test.assert_equals(move_zeros([0,0]),[0,0])
#Test.assert_equals(move_zeros([0]),[0])
#Test.assert_equals(move_zeros([False]),[False])
#Test.assert_equals(move_zeros([]),[])

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(move_zeros([0,1,None,2,False,1,0]))
print(move_zeros(["a","b"]))
print(move_zeros(["a"]))
print(move_zeros([0,0]))
print(move_zeros([0]))
print(move_zeros([False]))
print(move_zeros([]))

# Additional tests
# Output: ['y', True, 'x', -7, -10, 3, 10, 1, 0, 0, 0, 0]
print(move_zeros([0, 'y', True, 0, 'x', -7, -10, 3, 0, 0, 10, 1]))