"""
IQ Test
https://www.codewars.com/kata/552c028c030765286c00007d/train/python

Name: May Wang
Date: 23-Feb-2020
"""
def iq_test(numbers):
    # Add " " at the end of numbers
    numbers_tmp = numbers+" " 
    
    # Save numbers into list
    numbers_list = []
    i = 0   
    while(i < len(numbers_tmp)):
        for j in range(i+1,len(numbers_tmp)):
            if(numbers_tmp[j] == " "):
                numbers_list.append(int(numbers_tmp[i:j])%2)
                i = j+1
                break

    # Find only even/odd in the list
    count_even = 0
    for i in range(len(numbers_list)):
        if(numbers_list[i] == 0):
            count_even += 1
    if(count_even == 1):
        diff_index = numbers_list.index(0)+1
    else:
        diff_index = numbers_list.index(1)+1
    
    return diff_index

#Test.assert_equals(iq_test("2 4 7 8 10"),3)
#Test.assert_equals(iq_test("1 2 2"), 1)

print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 2"))
