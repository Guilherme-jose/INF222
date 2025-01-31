import time
import random

array = [random.uniform(0, 1000) for _ in range(1000000)]

start_time = time.time()
sorted_array = sorted(array)
end_time = time.time()

print("Time taken to sort:", end_time - start_time, "seconds")

def sort(array): # Algoritmo quicksort gerado pelo copilot
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return sort(left) + middle + sort(right)


start_time_custom = time.time()
sorted_array_custom = sort(array)
end_time_custom = time.time()

print("Time taken to sort with custom sort:", end_time_custom - start_time_custom, "seconds")


array_2m = [random.uniform(0, 1000) for _ in range(2000000)]

start_time_2m = time.time()
sorted_array_2m = sorted(array_2m)
end_time_2m = time.time()

print("Time taken to sort 2 million elements:", end_time_2m - start_time_2m, "seconds")

start_time_custom_2m = time.time()
sorted_array_custom_2m = sort(array_2m)
end_time_custom_2m = time.time()

print("Time taken to sort 2 million elements with custom sort:", end_time_custom_2m - start_time_custom_2m, "seconds")