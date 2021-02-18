def pascals_tri(num_rows):
    row_list_former = []
    row_list_current = []
    print(1)
    for row_num in range(num_rows):# FOR NEW ROWS        
        for current_num in range(len(row_list_former) + 1): # FOR NUM IN CURRENT ROW            
            if current_num == len(row_list_former):
                row_list_current.append(1)
                print(1, end = ' ')
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
# Goal Like this for input(8): ****





#           1
#          1 1
#         1 2 1
#        1 3 3 1
#       1 4 6 4 1
#     1 5 10 10 5 1 
#   1 6 15 20 15 6 1
#  1 7 21 35 35 21 7 1



# Num spaces before line = absolute value(reverse position of list index) - 1
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