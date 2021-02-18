def pascals_tri(num_rows): # Function prints num_rows rows of pascal's triangle
    row_list_former = []
    row_list_current = []
    print(1)
    for row_num in range(num_rows):# FOR NEW ROWS        
        for current_num in range(len(row_list_former) + 1): # FOR NUM IN CURRENT ROW            
            if current_num == len(row_list_former):
                row_list_current.append(1)
                print(1, end = ' ') # for printing the initial 1's for each row
                print(' ' * (num_rows - row_list_current[0]), end = '') # Aesthetic printing

                # FIXME: Add a section here that checks the max num of digits the list of the bottom row and base 
                # the num of spaces on that number: ie. if max digits per num in bottom row is 4 (ex. 3432) then
                # include 4 spaces before single digit numbers, 3 spaces before double digit... etc.
                
                for this_num in row_list_current:
                    print(this_num, end = ' ')
                print()
                break
            row_list_current.append(row_list_former[current_num - 1] + row_list_former[current_num])
        row_list_former = row_list_current
        row_list_current = []
    
user_num = input('Enter a whole number or enter q to quit:\n')
while user_num != 'q':
    if not user_num.isdigit():
        user_num = input('Enter a whole number or enter q to quit:\n')
        continue
    pascals_tri(int(user_num))
    user_num = input('Enter a whole number or enter q to quit:\n')

print('See ya!')


# Num spaces before line: spaces = num_rows - len(row_list_current)
#           x [-11] spaces: 10
#          x x [-10] spaces: 9
#         x x x [-9] spaces: 8
#        x x x x [-8] spaces: 7
#       x x x x x [-7] spaces: 6
#      x x x x x x [-6] spaces: 5
#     x x x x x x x [-5] spaces: 4
#    x x x x x x x x [-4] spaces: 3
#   x x x x x x x x x [-3] spaces: 2
#  x x x x x x x x x x [-2] spaces: 1
# x x x x x x x x x x x  [-1] spaces: 0