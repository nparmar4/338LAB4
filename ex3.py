# 1   The growth strategy used here is to overallocate memory proportional to the
#     current size of the list. This approach is used to avoid frequent reallocations
#     and copying of elements. The line "(newsize >> 3)" can be used to calculate the 
#     growth rate: (original size of the list (newsize)) + (1/8th of original size) +
#     (constant value of 6) all rounded up to the nearest multiple of 4. These lines - 
#     if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize))
#           new_allocated = ((size_t)newsize + 3) & ~(size_t)3;
#     state that If the difference between the new size and the old size is greater 
#     than the difference between the new allocated size and the new size, then the 
#     new allocated size is adjusted to be closer to the new size.

import timeit
import matplotlib.pyplot as plt

# Function to grow the array from size S to S+1
def grow_array(S):
    arr = list(range(S))
    arr.append(S)
    return arr

# Function to grow the array from size S-1 to S
def shrink_array(S):
    arr = list(range(S - 1))
    arr.append(S)
    return arr

S = 142  # Maximum bytes from question 2 is 568. 568/4 = 142 = largest int array size

# Reference: The following code is from ChatGPT
# Measure the time to grow the array from size S to S+1, repeated 1,000 times
time_measurements_grow = [timeit.timeit(lambda: grow_array(S), number=1) for _ in range(1000)]

# Measure the time to grow the array from size S-1 to S, repeated 1,000 times
time_measurements_shrink = [timeit.timeit(lambda: shrink_array(S), number=1) for _ in range(1000)]

# Plot the distribution of both measurements
plt.figure(figsize=(10, 6))
plt.hist(time_measurements_grow, alpha=0.5, label='Grow Array')
plt.hist(time_measurements_shrink, alpha=0.5, label='Shrink Array')
plt.title('Distribution of Time Measurements')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

#5   Although both growing and shrinking look similar on the histogram, growing the 
#    array takes a bit longer. Growing an array could take longer due to the need for 
#    memory reallocation, which involves finding contiguous memory (for successive elements). 