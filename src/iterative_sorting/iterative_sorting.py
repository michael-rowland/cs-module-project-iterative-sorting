def selection_sort(arr):
    for idx_i, i in enumerate(arr):
        idx_small, small = idx_i, i
        for idx_j, j in enumerate(arr[idx_i:]):
            if j < small:
                idx_small, small = idx_j, j
        if small != i:
            arr[idx_i], arr[idx_small+idx_i] = arr[idx_small+idx_i], arr[idx_i]
    return arr

# MY SOLUTION
def bubble_sort(arr):
    swapped = True
    unsorted = 0
    while swapped:
        swapped = False
        for i in range(len(arr[:-1]) + unsorted):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        unsorted -= 1
    return arr

# LOOKING AT STACK OVERFLOW
def bubble_sort(arr):
    length = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        length -= 1
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr