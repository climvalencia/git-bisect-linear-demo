from array import array

def sum_array_recursive(array):
    return sum_array_recursive1(array, 0)

def sum_array_recursive1(array, total):
    if len(array) < 1:
        return total
    else:
        return sum_array_recursive1(array, total + array.pop())

assert sum_array_recursive([1]) == 1
assert sum_array_recursive([]) == 0
assert sum_array_recursive(array('H', [1,2,3,4,5,6,7])) == 28
print "WORKS"
