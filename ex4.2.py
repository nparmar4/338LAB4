import timeit
import random
import matplotlib.pyplot as plt

#inefficient implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
#worst case complexity: O(n)

#efficient implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#worst case complexity: O(log n)


def experiment():
    n = 1000
    num_trials = 100
    linear_search_times = []
    binary_search_times = []

    for _ in range(num_trials):
        arr = sorted(random.sample(range(1, n*10), n))  # Generate a sorted array of length n
        target = random.randint(1, n*10)  # Generate a random target element

        linear_search_time = timeit.timeit(lambda: linear_search(arr, target), number=1)
        linear_search_times.append(linear_search_time)

        binary_search_time = timeit.timeit(lambda: binary_search(arr, target), number=1)
        binary_search_times.append(binary_search_time)

    plt.plot(linear_search_times, label='Linear Search')
    plt.plot(binary_search_times, label='Binary Search')
    plt.xlabel('Trial')
    plt.ylabel('Execution Time (s)')
    plt.title('Comparison of Linear Search and Binary Search')
    plt.legend()
    plt.show()

experiment()

#this code was generated using chatGPT but was significantly modified to portray accurate values