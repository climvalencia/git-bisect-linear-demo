
def sum_array_recursive(array):
    if len(array) == 1:
        return array.pop()
    else:
        return array.pop() + sum_array_recursive(array)

assert sum_array_recursive([1,2,3,4,5,6,7]) == 28
print "WORKS"
