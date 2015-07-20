from random import randint
from timeit import Timer
import cProfile
import pstats
import timeit
import random
import math



# Test data functions
def createIncreaseSorted(range):

    aList = []
    i = 0
    
    while i < range:
        aList.append(i)
        
        i += 1

    return aList


def createDecreaseSorted(range):

    aList = []
    i = range
    
    while i > 0:
        aList.append(i)
        
        i -= 1

    return aList


def createPartialIncreaseSorted(range):

    aList = []
    i = 0

    while i < range:
        
        if i % 10 == 0:
            aList.append(randint(0, 65535))
            
        else:
            aList.append(i)

        i += 1

    return aList


def createPartialDecreaseSorted(range):

    aList = []
    i = range

    while i > 0:
        
        if i % 10 == 0:
            aList.append(randint(0, 65535))
            
        else:
            aList.append(i)

        i -= 1

    return aList


def createEqual(range):

    a_random_int = randint(0, 65535)
    aList = []
    i = 0

    while i < range:
        aList.append(a_random_int)

        i += 1

    return aList


def createUShaped(range):

    aList = []
    i = range
    new_range = range*(.666)


    while i >= new_range:
        aList.append(i)
        
        i -= 1


    z = i
    new_range = range*(.333)

    while i > new_range:
        aList.append(z)

        i -= 1

    i = z
    new_range = range
    while i <= new_range:
        aList.append(i)

        i += 1

        if len(aList) == range:
            break

    return aList
        

def createRandom(range):

    aList = []
    i = 0

    while i < range:
        aList.append(randint(0, range - 1))

        i += 1

    return aList


def createEmpty():

    aList = []

    return aList


# End of test functions


# Sorting functions


# heapSort #1


def heapSort1(lst):
    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(lst)-2)/2, -1, -1):
        siftdown(lst, start, len(lst)-1)
    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst
 
def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


# End Hepsort #1


# Heapsort #2

def swap(series, i, j):
    series[i], series[j] = series[j], series[i]

def heapify(series, end, i):
    firstchild = 3*i + 1
    lastchild = min(firstchild + 3, end)
    children = list(range(firstchild, lastchild))
    maxelem = max((series[j], j) for j in [i] + children)
    maxval, maxindex = maxelem
    if maxindex != i:
        swap(series, i, maxindex)
        heapify(series, end, maxindex)

def heapSort2(series):
    end = len(series)
    start = end / 2 - 1
    for i in range(start, -1, -1):
        heapify(series, end, i)
    for i in range(end-1, 0, -1):
        swap(series, i, 0)
        heapify(series, i, 0)
    return series


# Quicksort #1
# Uses pivot at 0 of each sub array


def quickSort1(list_):
    """
    Iterative version of quick sort
    """

    if len(list_) <= 0:
        return list_


    left = 0
    right = len(list_) - 1
    temp_stack = []
    temp_stack.append((left,right))
    
    #Main loop to pop and push items until stack is empty
    while temp_stack:      
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))

    return list_

def partition(list_, left, right):
    """
    Partition method
    """
    #Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right
 
    while 1:
        while i <= j  and list_[i] <= piv:
            i +=1
        while j >= i and list_[j] >= piv:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    #Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j


# Quicksort #1
# Explicit stack
# Hoare partiton with median of 3 pivot

def quickSort2(list_):
    """
    Iterative version of quick sort
    """

    if len(list_) <= 0:
        return list_
    
    left = 0
    right = len(list_) - 1
    temp_stack = []
    temp_stack.append((left,right))
    
    #Main loop to pop and push items until stack is empty
    while temp_stack:      
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition2(list_,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))

    return list_


def median(a, i, j, k):
    if a[i] < a[j]:
        return j if a[j] < a[k] else k
    else:
        return i if a[i] < a[k] else k

def partition2(list_, left, right):
    """
    Partition method
    """
    #Pivot first element in the array
    pivotindex = median(list_, left, right, (left + right) // 2)
    list_[left], list_[pivotindex] = list_[pivotindex], list_[left]
    piv = list_[left]
    i = left + 1
    j = right
 
    while 1:

        while i <= j  and list_[i] <= piv:
            i +=1
        while j >= i and list_[j] >= piv:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    #Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j



# Mergesort #1
# Recursive implementation


def mergeSort1(alist):
    #print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort1(lefthalf)
        mergeSort1(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):

            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)
    return alist

# End Mergesort #1


# Mergesort #2
# Recursive implementation
# Uses insertion sort on sub-arrays at or below 7 elements
# Purpose increase 10-16%
# AKA Timsort

# Insertion sort 
def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items

# End insertion sort


def mergeSort2(alist):
    #print("Splitting ",alist)

    if len(alist) <= 7:
        insertion_sort(alist)


    else:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort2(lefthalf)
        mergeSort2(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)
    return alist

# End Mergesort #2

"""
# Probably won't use
# Mergesort 3
# Iterative implementation
def countMergeSort3():
    return
def mergeSort3(lst):
    if not lst:
        return []
    lists = [[x] for x in lst]
    while len(lists) > 1:
        lists = merge_lists(lists)
    return lists[0]
 
def merge_lists(lists):
    result = []
    for i in range(0, len(lists) // 2):
        result.append(merge2(lists[i*2], lists[i*2 + 1]))
    if len(lists) % 2:
        result.append(lists[-1])
    return result
 
def merge2(xs, ys):
    countMergeSort3()
    i = 0
    j = 0
    result = []
    while i < len(xs) and j < len(ys):
        x = xs[i]
        y = ys[j]
        if x > y:
            result.append(y)
            j += 1
        else:
            result.append(x)
            i += 1
    result.extend(xs[i:])
    result.extend(ys[j:])
    return result
# End Mergesort #3
"""



#Introsort

def introsort_loop(aList, lo, hi, depth_limit):

    while (hi - lo > 16):

        if depth_limit == 0:
            #print "Calling heapsort"
            heapSort1(aList)
            return aList

        depth_limit = depth_limit - 1
        #print "Calling partition"
        p = partition2(aList, lo, hi)
        introsort_loop(aList, p, hi, depth_limit)
        hi = p

def introsort(aList, begin, end):

    if begin < end:
        introsort_loop(aList, begin, end, math.floor(math.log(end-begin) * 2))
        insertion_sort(aList)


def heapSort3(aList):
    
    end = len(aList) - 1
    introsort(aList, 0, end)
    return aList



"""
def countMergeSort3():
    return
def MERGE(A,start,mid,end):
    L = A[start:mid]
    R = A[mid:end]
    i = 0
    j = 0
    k = start
    for l in range(k,end):
        countMergeSort3()
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  
def mergeSort3(aList):
    p = aList[0]
    r = len(aList) - 1
    mergeSort3a(aList, p, r) 
def mergeSort3a(A,p,r):
    if r - p > 1:
        mid = int((p+r)/2)
        mergeSort3a(A,p,mid)
        mergeSort3a(A,mid,r)
        MERGE(A,p,mid,r)
"""
"""
def countMergeSort5():
    return
def mergeSort5(array):
    n  = len(array)
    if n <= 1:
        return array
    left = array[:n/2]
    right = array[n/2:]
    return merge(mergeSort5(left),mergeSort5(right))
def merge(array1,array2):
    merged_array=[]
    while array1 or array2:
        countMergeSort5()
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
        else:
            merged_array.append(array2.pop())
    merged_array.reverse()
    return merged_array
"""

# Comparison of standard sort with our sorting algoritms
def sortComparison(range):

    aList = createRandom(range)
    aList1 = aList[:]
    aList2 = aList[:]
    aList3 = aList[:]
    aList4 = aList[:]
    aList5 = aList[:]
    aList6 = aList[:]
    aList7 = aList[:]
    
    aList1 = sorted(aList1)
    
    aList2 = mergeSort1(aList2)
    aList3 = mergeSort2(aList3)
    aList4 = heapSort1(aList4)
    aList5 = heapSort2(aList5)
    aList6 = quickSort1(aList6)
    aList7 = quickSort2(aList7)


    print "Results of standard sorting library comparison tests"
    print ""

    
    if aList1 != aList2:
        print "mergeSort1 is incorrect!"
        print aList2

    else:
        print "MergeSort1 passed!"


    if aList1 != aList3:
        print "mergeSort2 is incorrect!"
        print aList3

    else:
        print "MergeSort2 passed!"

    
    if aList1 != aList4:
        print "heapSort1 is incorrect!"
        print aList4

    else:
        print "heapSort1 passed!"

    
    if aList1 != aList5:
        print "heapSort2 is incorrect!"
        print aList5

    else:
        print "heapSort2 passed!"

    
    if aList1 != aList6:
        print "quickSort1 is incorrect!"
        print aList6

    else:
        print "quickSort1 passed!"
        

    if aList1 != aList7:
        print "quickSort2 is incorrect!"
        print aList7

    else:
        print "quickSort2 passed!"
    



def run_tests(sort_type, range, runs):
    
    print "Results for " + str(sort_type)

    aList = createIncreaseSorted(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort increasing data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)

    aList = createDecreaseSorted(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort decreasing data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)

    aList = createPartialIncreaseSorted(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort partially increasing data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)

    aList = createPartialDecreaseSorted(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort partially decreasing data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)

    aList = createEqual(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort equal data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)
    
    aList = createUShaped(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort U shaped data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)

    aList = createRandom(range)
    t = Timer(lambda: sort_type(aList))
    print "Average time to sort random data (" + str(range) + " data points " + str(runs) + " runs): " + str(t.timeit(number=runs)/runs)

    print "\n"
 
    
def run_profile(sort_type, range):

    print "Results for " + str(sort_type)

    aList = createIncreaseSorted(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for increasing sorted data"
    p.print_stats()

    aList = createDecreaseSorted(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for decreasing sorted data"
    p.print_stats()

    aList = createPartialIncreaseSorted(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for partially increasing sorted data"
    p.print_stats()

    aList = createPartialDecreaseSorted(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for partially decreasing sorted data"
    p.print_stats()

    aList = createEqual(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for equal sorted data"
    p.print_stats()

    aList = createUShaped(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for U shaped sorted data"
    p.print_stats()

    aList = createRandom(range)
    cProfile.runctx("sort_type(aList)", globals(), locals(), "stats")
    p = pstats.Stats('stats')
    print "Performance for random sorted data"
    p.print_stats()

    print ""
    print ""


# Test a single algorithm using data from 0 elements to 10^7 elements
def time_test_set(sort_type):

    # 0 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 0, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 0, 10)

    # 10^1 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 10, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 10, 10)

    # 10^2 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 100, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 100, 10)

    # 10^3 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 1000, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 1000, 10)

    # 10^4 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 10000, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 10000, 10)

    # 10^5 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 100000, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 100000, 10)

    # 10^6 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 1000000, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 1000000, 10)

    # 10^7 elements
    print "**************** Running warmup tests ****************"
    run_tests(sort_type, 10000000, 3)
    print "**************** Running regular tests ****************"
    run_tests(sort_type, 10000000, 10)

    

def my_tests():


    #sortComparison(0)
    
    print "*************** STARTING TIMED TEST SUITE ***************"
    print "******************** 00:00am  3/3/15 ********************"
    
    time_test_set(heapSort1)
    time_test_set(heapSort2)
    time_test_set(heapSort3)
    time_test_set(quickSort1)
    time_test_set(quickSort2)
    time_test_set(mergeSort1)
    time_test_set(mergeSort2)
    
    
    #run_tests(heapSort1, 100000, 10)
    #run_tests(heapSort2, 1000000, 1)
    #run_tests(quickSort1, 100000, 10)
    #run_tests(quickSort2, 100000, 10)
    #run_tests(mergeSort1, 100000, 10)
    #run_tests(mergeSort2, 100000, 10)

    #Still high
    #run_profile(heapSort1, 10000)

    #Still high
    #run_profile(heapSort2, 10000)

    #Good
    #run_profile(quickSort1, 10000)
    #Good
    #run_profile(quickSort2, 10000)

    #Still high
    #run_profile(mergeSort1, 10000)

    #Still high
    #run_profile(mergeSort2, 10000)

    #run_profile(mergeSort3, 10000)
    

 

my_tests()
