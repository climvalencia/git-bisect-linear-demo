# Entry point of our code

from array import array

def sum_array_iterative(array):
    total = 0
    for integer in array:
        total += integer
    return total

assert sum_array_iterative(array('H',[1,2,3,4,5,6,7])) == 28
print "WORKS"
