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
            space_left -= copy_cows[cow_with_max_weight(copy_cows)]
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

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:
    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    check_is_ship_big_enough(cows, limit)

    best_trips_exists = False

    for each_set in get_partitions(set(cows.keys())):
        for each_trip in each_set:
            if not can_fit(each_set, limit, cows):
                break
            else: 
                if best_trips_exists == False:
                    best_trips = each_set
                    best_trips_exists = True
                elif len(best_trips) > len(each_set):
                    best_trips = each_set
    return best_trips
            

def can_fit(trips, limit, cows):
    """True if every trip of set can fit set of cows, False otherwise"""
    overloaded = False
    for trip in trips:
        weight = int()
        for each in trip:
            weight += cows[each]
        if weight > limit:
            overloaded = True
            break

    if overloaded == True:
        return False
    else: return True
    

#TEST
#print  brute_force_cow_transport(load_cows(cow_data1))
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.
    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy_cow_transport(load_cows(cow_data1))
    end = time.time()
    print ("it took ", end-start,"sec for greedy algorithm on cow_data.txt")
    
    start = time.time()
    brute_force_cow_transport(load_cows(cow_data1))
    end = time.time()
    print ("it took ", end-start, "sec to brute force cow_data.txt")
    print
    
    start = time.time()
    greedy_cow_transport(load_cows(cow_data2))
    end = time.time()
    print ("it took ", end - start,"sec for greedy algorithm on cow_data_2.txt")
    
    start = time.time()
    brute_force_cow_transport(load_cows(cow_data2))
    end = time.time()
    print ("it took ", end - start, "sec to brute force cow_data_2.txt")

compare_cow_transport_algorithms()
