# Author: SCT (AMDG) 11/12/21

my_row = ['ryan', 'chris']

my_row[2:] = ['spencer']

my_row2 = my_row

print(my_row2)

del my_row[1]

print(my_row)
# my_row2 still prints the original list without the deleted element
