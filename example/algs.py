import numpy as np
# import time
# import matplotlib.pyplot as plt


def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1, 2, 3])


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
    else:
        n = len(x)
        while n > 0:
            last_sorted = 0
            for i in range(1, n):
                if x[i - 1] > x[i]:
                    temp = x[i - 1]
                    x[i - 1] = x[i]
                    x[i] = temp
                    last_sorted = i
            n = last_sorted
    return x


def quicksort(x):
    def qs_alg(x, l, r):
        if l < r:
            p = partition(x, l, r)
            qs_alg(x, l, p - 1)
            qs_alg(x, p + 1, r)
        return x

    def partition(x, l, r):
        pivot = x[l]
        i = l + 1
        j = r
        not_complete = True
        while not_complete:
            while i <= j and x[i] <= pivot:
                i += 1
            while i <= j and x[j] >= pivot:
                    j -= 1
            if j < i:
                not_complete = False
            else:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
        temp = x[l]
        x[l] = x[j]
        x[j] = temp
        return j

    if len(x) == 0:
        print('Zero-length list')
        return []
    elif len(x) == 2:
        if x[0] > x[1]:
            temp = x[0]
            x[0] = x[1]
            x[1] = temp
        return x
    else:
        qs_alg(x, 0, len(x) - 1)
        return x

# bs_times = []
# qs_times = []
# lengths = [100 * x for x in range(1, 11)]
# for length in lengths:
#     test_vecs = [np.random.randint(999, size=length) for x in range(0, 100)]
#     qs_times.append([])
#     bs_times.append([])
#     for vec in test_vecs:
#         test = list(vec)
#         # start = time.time()
#         # quicksort(test)
#         # end = time.time()
#         # qs_times[-1].append(end - start)
#         start = time.time()
#         bubblesort(test)
#         end = time.time()
#         bs_times[-1].append(end - start)

# print(len(bs_times))
# print(len(bs_times[0]))
# plt.close()
# plt.figure()
# print(np.asarray(bs_times))
# print(np.asarray(bs_times).mean(axis=1))
# plt.suptitle('Bubblesort Sorting Time Divided by N*N vs. Length of Vector')
# plt.xlabel('Vector Length (N)')
# plt.ylabel('Sorting Time Divided by N*N')
# to_plot = [np.asarray(bs_times).mean(axis=1)[i] / (lengths[i] *
#     lengths[i]) for i in range(0, len(lengths))]
# plt.plot(lengths, to_plot, 'ro--')
# plt.axhline(np.asarray(to_plot).mean())
# plt.show()
# plt.close()

test1 = [7, 3, 2, 8, 1, -1, 0, -1]
test2 = [8, 2, 6, 3, 3]
err1 = [1, 6, 2, 'a']
err2 = []
err3 = [1, 2, 3, 4, 5]
err4 = [1]
assert bubblesort(test1) == [-1, -1, 0, 1, 2, 3, 7, 8]
assert bubblesort(test2) == [2, 3, 3, 6, 8]
# assert bubblesort(err1) == []
# assert bubblesort(err2) == []
# assert bubblesort(err3) == [1, 2, 3, 4, 5]
# assert bubblesort(err4) == [1]
assert quicksort(test1) == [-1, -1, 0, 1, 2, 3, 7, 8]
assert bubblesort(test2) == [2, 3, 3, 6, 8]
# assert quicksort(err1) == []
# assert quicksort(err2) == []
# assert quicksort(err3) == [1, 2, 3, 4, 5]
# assert quicksort(err4) == [1]
