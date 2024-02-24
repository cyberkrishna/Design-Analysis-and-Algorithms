import random,time
def buble_sort(a):
    start_time = time.time()
    lenth= len(a)
    swap=0
    for i in range (lenth-1):
        for j in range(0, lenth -i-1 ):
            if a[j] > a [j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap+=1
    end_time = time.time()
    return a,swap,(end_time-start_time)*10000

a= random.sample(range(1,1000),100)
print("Original array is:",a)
[sorted,swap,timetaken]= buble_sort(a)
print("Bubble Sort :\n")
print("number of swaps :",swap)
print("Sorted elements:",sorted)
print("time take:",timetaken)

def insertion_sort(array):
    start_time =time.time()
    length= len(array)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    end_time = time.time()
    return array, (end_time - start_time)*10000

[b,timetaken]=insertion_sort(a)
print("\nInsertion Sort:\n")
print("Sorted elements:",b)
print("time take:",timetaken)

def selection_sort(array):
    start_time=time.time()
    for i in range(len(array)):
        min_element = array[i]
        min_index = i
        for j in range(i +  1, len(array), 1):
            if array[j] < min_element:
                min_element = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    end_time=time.time()
    return array, (end_time - start_time)*10000


def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000 

def get_execution_time(arr):
    execution_times = {}
    for sort_func in [buble_sort, insertion_sort, selection_sort]:
        arr_copy = arr.copy()
        execution_times[sort_func.__name__] = measure_time(sort_func, arr_copy)
    
    return execution_times
[c,timetaken]=selection_sort(a)
print("\nSelection Sort:\n")
print("Sorted elements:", c)
print("time take:",timetaken)
