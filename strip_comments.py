"""
Strip Comments
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

Name: May Wang
Date: 24-Feb-2020
"""
def solution(string,markers):
    # Add "\n" at the end of string
    string_tmp = string+"\n"
    
    # Do not copy comments into string_out
    string_out = ""   
    i = 0
    comments_pos = 0
    comments_pos_first = 0
    while(i < len(string_tmp)-1):
        j = i
        comments_count = 0
        while(string_tmp[j] != "\n"):
            # Case 0: First elem in sentence is in markers
            if(j == i) and (string_tmp[j] in markers):
                comments_pos = i-1
                comments_pos_first = i-1
                comments_count += 1
            # Case 1: others
            if(string_tmp[j+1] in markers):
                # Capture the first marker in each sentence
                if(comments_count == 0):
                    comments_pos = j
                    comments_pos_first = j
                else:
                    comments_pos = comments_pos_first
                comments_count += 1
            j += 1
        
        # Case 1
        if(comments_pos != i-1):
            # No markers
            if(comments_pos <= i):
                string_out += string_tmp[i:j]
            # Remove markers
            else:
                string_out += string_tmp[i:comments_pos]

        # Add "\n" at the end of each sentence except the last
        if(j < len(string_tmp)-1):
            string_out += "\n"
        i = j+1

    return string_out

#Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
#Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))

# Additional tests
# Output: ! avocados ?\navocados\nlemons @\nlemons bananas\nwatermelons pears '
print(solution("! avocados ?\navocados . apples watermelons\nlemons @ . watermelons\nlemons bananas\nwatermelons pears ' . strawberries bananas", ['.', '-']))

# Output:'\n\nstrawberries avocados bananas cherries lemons'
print(solution("- watermelons oranges\n# pears avocados avocados watermelons apples\nstrawberries avocados bananas cherries lemons", ['^', '#', '!', ',', "'", '-', '?']))
   
# Output: \n\nwatermelons bananas\n\nwatermelons
print(solution("? cherries oranges cherries !\n= avocados pears pears avocados\nwatermelons bananas\n^ ?\nwatermelons", ['.', ',', "'", '?', '@', '#', '=', '^']))
                                                                                                                         
# Output: pears\nbananas pears pears cherries strawberries\noranges lemons\napples avocados strawberries cherries oranges pears
print(solution("pears , '\nbananas pears pears cherries strawberries\noranges lemons = lemons apples\napples avocados strawberries cherries oranges pears", [',', '=', '#', "'", '.', '!', '^', '?', '@']))