#Question (1):
#Best Case Complexity: The best case complexity is O(n), we know this because the best case occurs when the list 
#li is either empty or contains elements only less than or equal to 5. In this particular scenario, the inner loop does
#not execute at all, thus resulting in a best case complexity, which would be O(n).

#Worst Case Complexity: The worst case complexity is O(n^2), we know this because the worst case occurs when every element in
#list li is greater than 5. Unlike the best case, in the worst case the inner loop will execute for ever element in the list,
#thus results in a complexity of O(n^2). 

#Average Case Complexity: The complexity will be between O(n) and O(n^2) for the average case. We know this because the 
#average case occurs when some elements in the list will be greater than 5 and some won't. In this scenario, the inner loop 
#executes for some elements but not all of them. Thus, we get a complexity between O(n) and O(n^2) that is dependent on the 
#distribution of elements greater than 5 in the list li.


#Question (2):
#The average, best, and worst case complexities are not the same for the provided code. To make them equivalent, we remove 
#the nested loop.

def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2
#chatgpt was used to generate this code




