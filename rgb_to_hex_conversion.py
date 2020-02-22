"""
RGB to Hex Conversion
Date: 22-Feb-2020
"""
def dec2hex(a):
    if(a < 0):
        a_hex_tmp_l = hex(0)
    elif(a > 255):
        a_hex_tmp_l = hex(255)
    else:
        a_hex_tmp_l = hex(a)
    a_hex_tmp_u = a_hex_tmp_l.upper()
    a_hex_list = list(a_hex_tmp_u)  
    if(len(a_hex_tmp_u) == 3):
        a_hex_list.pop(1)
    else:
        a_hex_list.pop(0)
        a_hex_list.pop(0)
    a_hex = ""
    for i in range(2):
        a_hex += a_hex_list[i]
    return a_hex

def rgb(r, g, b):
    #your code here :)
    r_hex = dec2hex(r)
    g_hex = dec2hex(g)
    b_hex = dec2hex(b)
    rgb_hex = r_hex+g_hex+b_hex
    return rgb_hex

#test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
#test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
#test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
#test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
#test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

print(rgb(0,0,0))
print(rgb(1,2,3))
print(rgb(255,255,255))
print(rgb(254,253,252))
print(rgb(-20,275,125))