# Question 1

Several factors can cause noise or inaccuracies into the measurement. Timing issues can occur when the execution time of a component varies depending on the input, the processor speed, the interrupt frequency, or the system load. These issues can cause unexpected behavior, errors, or failures in the software, and can be hard to detect and reproduce in unit testing. 

The timeit.timeit() function, with the number parameter, executes the provided code a specified number of times and calculates the total elapsed time. This approach helps mitigate noise by averaging out variations in execution time and providing a more stable measurement. This is appropriate for scenarios where you need a quick and simple way to measure the code's performance and do not require detailed statistics.

On the other hand, the timeit.repeat() function executes the provided code multiple times and repeats the measurement a specified number of times. Repeating the measurement across multiple trials is useful when you want to assess the variability of execution time across multiple runs. This helps mitigate outliers and provides a more reliable estimate of the code's performance under various conditions. Use this function when you need a more detailed analysis of the code's performance.


# Question 2

The appropriate statistic for timeit.timeit() is average. This is because it is used to measure the execution time of a specific code segment over multiple iterations. By dividing the total elapsed time by the number of iterations, it returns the average time taken for each iteration.

For timeit.repeat(), all three (minimum, maximum, and average) are appropriate statistics. This is because it repeats all three of the measurements a specified number of times. The minimum time captures the best-case scenario (optimal performance). The maximum time identifies outliers (degraded performance). The average time gives a general overview of the code's typical performance across repetitions. 

# References
1. https://stackoverflow.com/questions/56763416/what-is-diffrence-between-number-and-repeat-in-python-timeit 

2. https://www.linkedin.com/advice/1/how-do-you-deal-concurrency-timing#:~:text=Timing%20issues%20can%20occur%20when,and%20reproduce%20in%20unit%20testing.

3. ChatGPT
