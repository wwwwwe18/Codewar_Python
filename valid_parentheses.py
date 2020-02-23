"""
Valid Parentheses
https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

Name: May Wang
Date: 23-Feb-2020
"""
def valid_parentheses(string):
    #your code here
    out = False
    
    # Define a list
    # "(": -1
    # ")": +1
    # Others: N/A
    string_list = []
    
    # 0 <= len(string) <= 200
    if(len(string) >= 0) and (len(string) <= 200):
        for i in range(len(string)):
            if(string[i] == "("):
                string_list.append(-1)
            elif(string[i] == ")"):
                string_list.append(1)
        
        # Num of "(" and ")": identical
        if(sum(string_list) == 0):
            # Empty case: Return True
            if(len(string) == 0):
                out = True
            else:
                # Case: first elem is "(" and last elem is ")" in list
                if(string_list[0] == -1) and (string_list[len(string_list)-1] == 1):                    
                    # Calculate the sum of first few elem
                    for i in range(len(string_list)):
                        if(sum(string_list[0:i+1]) != 1):
                            out = True
                        # False if sum = 1 happens
                        else:
                            out = False
                            break
    return out

#Test.assert_equals(valid_parentheses("  ("),False)
#Test.assert_equals(valid_parentheses(")test"),False)
#Test.assert_equals(valid_parentheses(""),True)
#Test.assert_equals(valid_parentheses("hi())("),False)
#Test.assert_equals(valid_parentheses("hi(hi)()"),True)

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))

# Additional tests
print(valid_parentheses(")((hi))("))
print(valid_parentheses("hi((hi)))("))
print(valid_parentheses("yp(x)()ewxbbiog"))
print(valid_parentheses("v()((rv))e)bik(cv(ni)gw"))