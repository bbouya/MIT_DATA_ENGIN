# EL

from ps1_partition import get_partitions
import time

cow_data1 = 'ps1_cow_data.txt'
cow_data2 = 'ps1_cow_data_2.txt'

# Transporting Spaces

# First problem solution to
# Read a file line by line

def load_cows(filname):
    #ToDo Spaces
    cow_file = open(filname, 'r')
    cow_dic = dict()
    for line in cow_file:
        line_listed = line.split(',')
        line_listed[1] = int(line_listed[1].strip('\n'))
        cow_dic[line_listed[0]] = line_listed[1]
    return cow_dic

#for the test print some line of filname.txt
print(load_cows(cow_data1))