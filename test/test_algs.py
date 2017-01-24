import numpy as np
from example import algs

test1 = [7, 3, 2, 8, 1, -1, 0, -1]
test2 = [8, 2, 6, 3, 3]
err2 = []
err3 = [1, 2, 3, 4, 5]
err4 = [1]


def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1, 2, 3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1, 2, 3]))


def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1, 2, 4, 0, 1])
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    assert algs.bubblesort(test1) == [-1, -1, 0, 1, 2, 3, 7, 8]
    assert algs.bubblesort(test2) == [2, 3, 3, 6, 8]
    assert algs.bubblesort(err2) == []
    assert algs.bubblesort(err3) == [1, 2, 3, 4, 5]
    assert algs.bubblesort(err4) == [1]
    assert algs.bubblesort(x) == [0, 1, 1, 2, 4]


def test_quicksort():

    x = np.array([1, 2, 4, 0, 1])
    # for now, just attempt to call the quicksort function, should
    # actually check output
    assert algs.quicksort(test1) == [-1, -1, 0, 1, 2, 3, 7, 8]
    assert algs.bubblesort(test2) == [2, 3, 3, 6, 8]
    assert algs.quicksort(err2) == []
    assert algs.quicksort(err3) == [1, 2, 3, 4, 5]
    assert algs.quicksort(err4) == [1]
    assert algs.quicksort(x) == [0, 1, 1, 2, 4]
