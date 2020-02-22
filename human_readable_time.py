"""
Human Readable Time
Date: 22-Feb-2020
"""
def len1to2(a):
    a_str = str(a)
    if(len(a_str) == 1):
        b = "0"+a_str
    else:
        b = a_str
    return b

def make_readable(seconds):
    # Do something
    t_h_tmp = int(seconds/3600)
    t_m_tmp = int((seconds-t_h_tmp*3600)/60)
    t_s_tmp = seconds-t_h_tmp*3600-t_m_tmp*60
    
    t_h = len1to2(t_h_tmp)
    t_m = len1to2(t_m_tmp)
    t_s = len1to2(t_s_tmp)
    
    t = t_h+":"+t_m+":"+t_s
    return t

#Test.assert_equals(make_readable(0), "00:00:00")
#Test.assert_equals(make_readable(5), "00:00:05")
#Test.assert_equals(make_readable(60), "00:01:00")
#Test.assert_equals(make_readable(86399), "23:59:59")
#Test.assert_equals(make_readable(359999), "99:59:59")

print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))