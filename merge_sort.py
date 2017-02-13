"""
-- Merge Sort Algorithm --
Takes an unordered list of size 'n' and sorts it
O(n) = n log n; Omega(n) = n log n
"""

def test(size, rang, sd):
    """
    Helper function for testing
    Inputs 'size', 'range' of integers and 'seed' for the random function
    """
    seed(sd)
    lst = []
    for _ in range(size + 1):
        lst.append(randrange(rang))
    print lst
    print merge_sort(lst)

def merge(array1, array2):
    """
    Helper function to merge the halves of the lists in order
    """
    temp = []
    len1, len2 = len(array1), len(array2)
    num1, num2 = 0, 0
    loop = False
    while loop == False:
        if num1 == len1:
            temp.append(array2[num2])
            num2 += 1
        elif num2 == len2:
            temp.append(array1[num1])
            num1 += 1
        elif array1[num1] < array2[num2]:
            temp.append(array1[num1])
            num1 += 1
        else:
            temp.append(array2[num2])
            num2 += 1
        if num1 == len1 and num2 == len2:
            loop = True
    return temp

def merge_sort(array):
    """
    Main function to split and merge the list in order using recursion
    """
    if len(array) <= 1:
        return array

    else:
        half = len(array) // 2
        left = array[:half]
        right = array[half:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

# Uncoment below to test
# from random import randrange, seed
# test(100, 100, 0)
