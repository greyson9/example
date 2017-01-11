import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
# input: a list of integers, x
# output: a sorted list (low to high) with the elements of x
# first, check to make sure the list is of appropriate size and content
# then, for each adjacent pair of elements, swap them 
# and store the current index (the rest of the list is already sorted)
# if the current index is 0, then nothing remains to be sorted

    if len(x) == 0:
        print('Zero-length list')
        return []
    elif any(not isinstance(mem, int) for mem in x):
        print('List contains non-integer element')
        return []
    else:
        n = len(x)
        while n > 0:
            last_sorted = 0
            for i in range(1, n):
                if x[i-1] > x[i]:
                    temp = x[i-1]
                    x[i-1] = x[i]
                    x[i] = temp
                    last_sorted = i
            n = last_sorted
    assert 1 == 1
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    """

    assert 1 == 1
    return

