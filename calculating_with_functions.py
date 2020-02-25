"""
Calculating with Functions
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

Name: May Wang
Date: 25-Feb-2020
"""
# Define the calculation
def output(a, func, b):
    if(func == "+"):
        out = a + b
    if(func == "-"):
        out = a - b
    if(func == "*"):
        out = a * b
    # Output int
    if(func == "/"):
        out = a // b
    return out

# Define num 0 - 9
def zero(arg = None):
    out = 0
    if(arg != None):
        a = 0
        [func, b] = arg
        out = output(a, func, b)
    return out
    
def one(arg = None):
    out = 1
    if(arg != None):
        a = 1
        [func, b] = arg
        out = output(a, func, b)
    return out

def two(arg = None):
    out = 2
    if(arg != None):
        a = 2
        [func, b] = arg
        out = output(a, func, b)
    return out

def three(arg = None):
    out = 3
    if(arg != None):
        a = 3
        [func, b] = arg
        out = output(a, func, b)
    return out

def four(arg = None):
    out = 4
    if(arg != None):
        a = 4
        [func, b] = arg
        out = output(a, func, b)
    return out

def five(arg = None):
    out = 5
    if(arg != None):
        a = 5
        [func, b] = arg
        out = output(a, func, b)
    return out

def six(arg = None):
    out = 6
    if(arg != None):
        a = 6
        [func, b] = arg
        out = output(a, func, b)
    return out

def seven(arg = None):
    out = 7
    if(arg != None):
        a = 7
        [func, b] = arg
        out = output(a, func, b)
    return out

def eight(arg = None):
    out = 8
    if(arg != None):
        a = 8
        [func, b] = arg
        out = output(a, func, b)
    return out

def nine(arg = None):
    out = 9
    if(arg != None):
        a = 9
        [func, b] = arg
        out = output(a, func, b)
    return out

# Define operation: + - * /
def plus(num):
    func = "+"
    b = num
    return func, b

def minus(num):
    func = "-"
    b = num
    return func, b

def times(num):
    func = "*"
    b = num
    return func, b

def divided_by(num):
    func = "/"
    b = num
    return func, b

#Test.describe('Basic Tests')
#Test.assert_equals(seven(times(five())), 35)
#Test.assert_equals(four(plus(nine())), 13)
#Test.assert_equals(eight(minus(three())), 5)
#Test.assert_equals(six(divided_by(two())), 3)

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))