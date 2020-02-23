"""
Dubstep
https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python

Name: May Wang
Date: 23-Feb-2020
"""
def song_decoder(song):
    if(len(song) <= 200):
        # Add WUB at tne end of song
        song += "WUB"
        if(song[0:3] == "WUB"):
            song_list = [" "]
            i = 3
        else:
            song_list = [""]
            i = 0
        
        count = 0
        
        # Copy song into list and replace "WUB" by " "
        while(i <= len(song)-1):
            if(song[i:i+3] != "WUB"):
                song_list[count] += song[i]
                
                if(song[i+1:i+3] != "WU"):
                    song_list[count] += song[i+1]
                    
                    if(song[i+2] != "W"):
                        song_list[count] += song[i+2]
                        i += 3
                    else:
                        i += 2
                else:
                    i += 1
            else:
                if(i <= len(song)-4):
                    song_list.append(" ")
                    count += 1
                i += 3
        
        # Remove " " from list
        song_list_tmp = song_list.copy()
        for i in range(len(song_list)):
            if(song_list[i] == " "):
                song_list_tmp.remove(" ")
        
        # Check the first one word with WUB
        song_list_start = song_list_tmp[0]
        if(song_list_tmp[0][0] == " "):
            song_list_tmp[0] = song_list_start[1:]
        
        # Generate outputs
        out = ""
        for i in range(len(song_list_tmp)):
            out += song_list_tmp[i]

    return out

#Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
#Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
#Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")

print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))

# Additional tests
print(song_decoder("WUBAAWUBBBWUBCCWUB"))
print(song_decoder("WUBWUBAAWUBBBWUBCCWUB"))