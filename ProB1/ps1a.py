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
#print(load_cows(cow_data1))


# Problem 2
def check_is_ship_big_enough(cows, limit):
    if cows[cow_with_max_weight(cows)] > limit:
        raise NameError('The ship is to small for the fattest cow')
    
def greedy_cow_transport(cows, limit = 10):
    copy_cows = dict(cows)
    trips = list()

    check_is_ship_big_enough(cows, limit)

    while len(copy_cows) != 0:
        space_left = int(limit)
        trip = list()
        while len(copy_cows) > 0 and space_left >= copy_cows[cow_with_min_weight(copy_cows)]:

            trip.append(cow_with_max_weight(copy_cows))
            space_left -= copy_cows[cow_with_lax_weight(copy_cows)]
            copy_cows.pop(cow_with_max_weight(copy_cows))
        trips.append(trip)
    return trips

def cow_with_max_weight(cows):

    weights = list(cows.values())
    cows_keys = list(cows.keys())
    return cows_keys[weights.index(max(weights))]

def cow_with_min_weight(cows):
    weight = list(cows.values())
    cows_keys = list(cows.keys())
    return cows_keys[weight.index(min(weight))]
#Test our problem 2 
print(cow_with_max_weight(load_cows(cow_data1)))
print(cow_with_min_weight(load_cows(cow_data1)))