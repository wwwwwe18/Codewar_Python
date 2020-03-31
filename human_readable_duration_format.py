"""
Human readable duration format
https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

Name: May Wang
Date: 31-Mar-2020
"""
# Rules:
# - years, days, hours, minutes and seconds; 
# - now for 0

def format_duration(seconds):
    # Zero case
    if(seconds == 0):
        out = "now"
    # Other cases
    if(seconds > 0):
        char = ["year","day","hour","minute","second"]
        
        # Save into year, day, hour, minute, second
        time = [0,0,0,0,0]
        time[0] = int(seconds/(60*60*24*365))
        time[1] = int((seconds-time[0]*(60*60*24*365))/(60*60*24))
        time[2] = int((seconds-time[0]*(60*60*24*365)-time[1]*(60*60*24))/(60*60))
        time[3] = int((seconds-time[0]*(60*60*24*365)-time[1]*(60*60*24)-time[2]*(60*60))/60)
        time[4] = seconds%60
        
        # Count non-zero elements
        count = 0
        out_index = []
        for i in range(len(time)):
            if(time[i]):
                out_index.append(i)
                count += 1
        
        # Generate out
        out = ""
        if(count == 1):
            out += str(time[out_index[0]])
            out += " "
            out += char[out_index[0]]
            if(time[out_index[0]] > 1):
                out += "s"
        else:
            for i in range(count):
                out += str(time[out_index[i]])
                out += " "
                out += char[out_index[i]]
                if(time[out_index[i]] > 1):
                    out += "s"
                if(i < count-1):
                    if(i == count-2):
                        out += " and "
                    else:
                        out += ", "
        
    return out

#test.assert_equals(format_duration(1), "1 second")
#test.assert_equals(format_duration(62), "1 minute and 2 seconds")
#test.assert_equals(format_duration(120), "2 minutes")
#test.assert_equals(format_duration(3600), "1 hour")
#test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")

print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))

# Additional tests
print(format_duration(0))
print(format_duration(360271))