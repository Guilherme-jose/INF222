import random
import time


setting = [-1,-1,-1,-1] # Algorithm, Size, Ordered, Uniform


def test(setting):
    if setting[1] == -1: size = 10000000
    else: size = 20000000
    
    random_list = []
    
    if setting[3] == 1: 
        num_negatives = size // 3
        num_positives = size // 3
        num_zeroes = size - num_negatives - num_positives
        
        random_list = (
            [random.uniform(-1000, -1) for _ in range(num_negatives)] +
            [random.uniform(1, 1000) for _ in range(num_positives)] +
            [0 for _ in range(num_zeroes)]
        )
    else:
        num_zeroes = size // 20
        num_non_zeroes = size - num_zeroes
        random_list = (
            [random.uniform(-1000, 1000) for _ in range(num_non_zeroes)] +
            [0 for _ in range(num_zeroes)]
        )
    
    random.shuffle(random_list)
    
    if setting[2] == 1: 
        for i in range(1000):
            start = random.randint(0, len(random_list) - 1001)
            end = start + 1000
            random_list[start:end] = sorted(random_list[start:end])
    
    start_time = time.time()
    
    if setting[0] == -1: 
        random_list.sort()
    else:
        def dutch_flag_partition(arr):
            low, mid, high = 0, 0, len(arr) - 1
            while mid <= high:
                if arr[mid] < 0:
                    arr[low], arr[mid] = arr[mid], arr[low]
                    low += 1
                    mid += 1
                elif arr[mid] > 0:
                    arr[mid], arr[high] = arr[high], arr[mid]
                    high -= 1
                else:
                    mid += 1

        dutch_flag_partition(random_list)
    
    end_time = time.time()
    
    print(f"Setting: {setting}")
    print(f"Execution time: {end_time - start_time} seconds")
    
def test_all_combinations():
    #for uniform in [-1, 1]:
        for ordered in [-1, 1]:
            for size in [-1, 1]:
                for algorithm in [-1, 1]:
                    setting = [algorithm, size, ordered, 1]
                    test(setting)

for i in range(5):                    
    test_all_combinations()
    print("Done")
    pass


# 2^5-2
print("2^5-2")
t = [
    [-1,  1, -1,  1],
    [ 1,  1, -1, -1],
    [-1, -1,  1,  1],
    [ 1, -1,  1, -1],
]

for setting in t:
    test(setting)
    print("Done")
    pass