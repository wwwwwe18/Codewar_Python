"""
Battleship field validator
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

Name: May Wang
Date: 1-Apr-2020
"""
# Rules:
# - There must be single battleship (size of 4 cells), 2 cruisers (size 3),
#   3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are
#   not allowed, as well as missing ships.
# - Each ship must be a straight line, except for submarines, which are just
#   single cell.
# - The ship cannot overlap or be in contact with any other ship, neither by edge
#   nor by corner.

# Sub-function: search for 1 battleship, 2 cruisers, 3 destroyers and 4 submarines
def check_field(field,array,row_column):
    num = [0,0,0,0]
    check_len = [1,2,3,4]
    for i in range(10):
        if(len(array[i])):
            for j in array[i]:
                sum_array = [0,0,0,0]
                sum_line = [0,0,0,0]
                for k in range(4):
                    for a in range(-1,2):
                        for b in range(-1,1+check_len[k]):
                            if(i+a >= 0) and (i+a <= 9) and (j+b >= 0) and (j+b <= 9):
                                # Check the non-zeros in array
                                if(row_column == "row"):
                                    sum_array[k] += field[i+a][j+b]
                                if(row_column == "column"):
                                    sum_array[k] += field[j+b][i+a] 
                        
                                # Check the non-zeros in line
                                if(a == 0) and (b >= 0) and (b < check_len[k]):
                                    if(row_column == "row"):
                                        sum_line[k] += field[i+a][j+b]
                                    if(row_column == "column"):
                                        sum_line[k] += field[j+b][i+a]

                    if(sum_array[k] == k+1) and (sum_line[k] == k+1):
                        num[k] += 1
    
    return num

def validate_battlefield(field):
    # Count total number and save non-zero position
    count = 0
    row = [[],[],[],[],[],[],[],[],[],[]]
    column = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        for j in range(10):
            if(field[i][j] == 1):
                row[i].append(j)
                column[j].append(i)
                count += 1

    out = False
    if(count == 4*1+3*2+2*3+1*4): 
        # Search in row
        row_result = check_field(field,row,"row")       
        # Search in column
        column_result = check_field(field,column,"column")
        
        if(row_result[0] == 4) and (row_result[1]+column_result[1] == 3) and (row_result[2]+column_result[2] == 2) and (row_result[3]+column_result[3] == 1):  
            out = True
    
    return out

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#Test.assert_equals(validate_battlefield(battleField), True, "Yep! Seems alright", "Nope, something is wrong!");

print(validate_battlefield(battleField))