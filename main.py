def first_pascal_rows(num_rows):
    row_list_former = []
    row_list_current = []

    for num in range(num_rows): # Veritcally down ****
        if num == 0:
            # 1 
        elif num == 1:
            # row_number (0, 1, 2, 3 // not 1, 2, 3)
        elif num == 2:
            # 

        print(num_rows)






first_pascal_rows(3)

# for each new number based on # from previous row

# for i in range(num_rows)   // 0    # FOR NEW ROWS
    # for current_num in range len(row_list_former + 1)    // 0    # FOR NUM IN CURRENT ROW
#       if current_num == len(row_list_former):
            # row_list_current[]
#       row_list_current[current_num] = row_list_former[current_num - 1] + row_list_former[current_num] 




# Goal Like this for input(8): ****

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1





#           1
#          1 1
#         1 2 1
#        1 3 3 1
#       1 4 6 4 1
#     1 5 10 10 5 1 
#   1 6 15 20 15 6 1
#  1 7 21 35 35 21 7 1