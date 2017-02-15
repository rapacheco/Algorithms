"""
-- Bynary Search Algorithm --
Takes an ordered list of size 'n' and looks for a specific element on it
O(n) = log n; Omega(n) = 1
"""

def test(size, rang, sd, target):
    """
    Helper function for testing
    Inputs 'size', 'range' of integers and 'seed' for the random function
    """
    seed(sd)
    lst = []
    for _ in range(size):
        lst.append(randrange(rang))
    print lst
    lst = merge_sort(lst)
    print lst
    print bynary(lst, target)

def bynary(array, target):
    """
    Main function for the algorithm
    Traverses the list with a divide and conquer approach until target is found
    Uses recursion technique
    """
    if len(array) <= 0:
        return "Target not found."

    mid_point = len(array) // 2
    mid_element = array[mid_point]
    if mid_element == target:
        return "Target found."

    else:
        if target > mid_element:
            new_array = array[mid_point:]
            return bynary(new_array, target)
        else:
            new_array = array[:mid_point]
            return bynary(new_array, target)
    return 0

# Uncoment below to test
# from random import randrange, seed
# from merge_sort import merge_sort
# test(11, 50, 0, 39)
