"""
Text align justify
https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python

Name: May Wang
Date: 30-Mar-2020
"""
# Here are the rules:
#
# - Use spaces to fill in the gaps between words.
# - Each line should contain as many words as possible.
# - Use '\n' to separate lines.
# - Gap between words can't differ by more than one space.
# - Lines should end with a word not a space.
# - '\n' is not included in the length of a line.
# - Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# - Last line should not be justified, use only one space between words.
# - Last line should not contain '\n'
# - Strings with one word do not need gaps ('somelongword\n').

# Sub-function: generate line
def generate_line(word_list,line_start,num_word,num_space): 
    # Generate list for spaces
    space_list = []
    # One/Two words in line with spaces
    if(num_word <= 2):
        space_string = ""
        if(num_space > 0):
            for i in range(num_space):
                space_string += " "
            space_list.append(space_string)
    else:
        space_line = int(num_space/(num_word-1))
        space_last_line = num_space-space_line*(num_word-1)
        
        for i in range(num_word-1):
            space_list.append("")
        
        # Last line should not be justified, use only one space between words.
        if(line_start+num_word == len(word_list)):
            for i in range(num_word-1):
                space_list[i] += " "
        else:
            for i in range(space_line):
                for j in range(num_word-1):
                    space_list[j] += " "
            for i in range(space_last_line):
                space_list[i] += " "
        
    space_list.append("")
            
    line = ""
    for j in range(num_word):
        line += word_list[line_start+j]
        if(num_word > 1):
            line += space_list[j]
    
    if(line_start+num_word < len(word_list)):
        line += "\n"

    return line

# Main function
def justify(text, width):
    # Add " " at the end of text
    text_tmp = text+" "
    
    # Calculate the length of each words
    word_len = []
    word_list = []
    word_start = 0
    for i in range(len(text_tmp)):
        if(text_tmp[i] == " "):
            word_len.append(i-word_start)
            word_list.append(text_tmp[word_start:i])
            word_start = i+1
    
    if(word_list[0] == "") or (word_list[len(word_list)-1] == ""):
        word_list.remove("")
        word_len.remove(0)
    
    out = ""
    line_list = []
    line_start = 0
    line_count_old = 0
    line_count = 0
    num_word = 0
    num_space = 0
    
    i = 0
    while(i <= len(word_len)-1):
        line_count_old = line_count       
        line_count += word_len[i]
        num_word += 1
        
        if(line_count+num_word-1 <= width):
            if(i == len(word_len)-1):
                num_space = width-line_count
                line_list.append(generate_line(word_list,line_start,num_word,num_space))
            i += 1
        else:
            i -= 1
            num_word -= 1
            num_space = width-line_count_old
            line_list.append(generate_line(word_list,line_start,num_word,num_space))
            
            # Reset for next line
            i = line_start+num_word
            line_start = line_start+num_word
            line_count_old = 0
            line_count = 0
            num_word = 0
            
    for i in line_list:
        out += i
    
    return out

#test.assert_equals(justify('123 45 6', 7), '123  45\n6')

#print(justify('123 45 6', 7))

# Additional tests
print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.',100))