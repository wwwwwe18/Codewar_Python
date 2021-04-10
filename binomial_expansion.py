"""
Binomial Expansion
https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python

Name: May Wang
Date: 10-Apr-2021
"""
# (ax+b)^n = ax^b+cx^d+ex^f...
# (x+y)^n = (n!/(k!*(n-k)!))*(x^(n-k))*(y^k)
#
# Example
# expand("(2f+4)^6")
# returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"

def expand(expr):
    import math
    
    # Step 0: "x" to "1x"; "-x" to "-1x"
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    # "x" to "1x"
    if(ascii_lowercase.rfind(expr[expr.rfind('(')+1]) > 0):
        expr_list = [expr[0:expr.rfind('(')+1],'1',expr[expr.rfind('(')+1:]]
        expr = ''.join(expr_list)
    # "-x" to "-1x"
    elif(ascii_lowercase.rfind(expr[expr.rfind('(')+2]) > 0):        
        if(expr[expr.rfind('(')+1] == '-'):
            expr_list = [expr[0:expr.rfind('(')+2],'1',expr[expr.rfind('(')+2:]]    
            expr = ''.join(expr_list)
        
    # Step 1: Find a,b,n
    for i in range(len(expr)):
        if(expr[i] == '('):
            x_st = i+1
        elif(ascii_lowercase.rfind(expr[i]) >= 0):
            x_ascii = expr[i]
            x_ed = i-1
            y_st = i+1
        elif(expr[i] == ')'):
            y_ed = i-1            
        elif(expr[i] == '^'):
            n_st = i+1
    
    a = int(expr[x_st:x_ed+1])
    b = int(expr[y_st:y_ed+1])
    n = int(expr[n_st:])
    
    # Step 2: Generate total coefficient and output string
    if(n == 0):
        out_str = '1'
    else:
        k_list = []
        for i in range(n+1):
            binomial_co_k = int(math.factorial(n)/(math.factorial(n-i)*math.factorial(i)))
            total_co_k = binomial_co_k*(a**(n-i))*(b**(i))
            total_co_k_str = str(total_co_k)
        
            if(i == 0):
                # "1x"
                if(total_co_k == 1):
                    total_co_k_str = ''
                # "-1x"
                if(total_co_k == -1):
                    total_co_k_str = '-'                
            elif(total_co_k > 0):
                total_co_k_list = [total_co_k_str]
                total_co_k_list.insert(0,'+')
                total_co_k_str = ''.join(total_co_k_list)
            
            if((n-i) > 1):
                k = [total_co_k_str,x_ascii,'^',str(n-i)]
            elif((n-i) == 1):
                k = [total_co_k_str,x_ascii]
            else:
                k = [total_co_k_str]
            
            k_list.append(''.join(k))

        out_str = ''.join(k_list)         

    return out_str

#test.assert_equals(expand("(x+1)^0"), "1")
#test.assert_equals(expand("(x+1)^1"), "x+1")
#test.assert_equals(expand("(x+1)^2"), "x^2+2x+1")

#test.assert_equals(expand("(x-1)^0"), "1")
#test.assert_equals(expand("(x-1)^1"), "x-1")
#test.assert_equals(expand("(x-1)^2"), "x^2-2x+1")

#test.assert_equals(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
#test.assert_equals(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
#test.assert_equals(expand("(7x-7)^0"), "1")

#test.assert_equals(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
#test.assert_equals(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
#test.assert_equals(expand("(-7x-7)^0"), "1")

print(expand("(-w-16)^1"))

print(expand("(x+1)^0"))
print(expand("(x+1)^1"))
print(expand("(x+1)^2"))

print(expand("(x-1)^0"))
print(expand("(x-1)^1"))
print(expand("(x-1)^2"))
    
print(expand("(5m+3)^4"))
print(expand("(2x-3)^3"))
print(expand("(7x-7)^0"))

print(expand("(-5m+3)^4"))
print(expand("(-2k-3)^3"))
print(expand("(-7x-7)^0"))