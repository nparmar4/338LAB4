# Question 1

    Linked Lists:
        Advantages:
            - can grow and shrink without resizing
            - dynamic memory allocation (no space wasted)
            - - efficient for insertions and deletions

        Disadvantages:
            - slow sequiential access 
            - takes up alot of space in memory due to need for pointer with every element 
    
    Arrays:
        Advantages: 
            - easy access to all elements 
            - chache-friendly 

        Disadvantages: 
            - fixed size, and must be manually resized if needed
            - not effective for intertion or deletion in the middle (hard to shift)

# Question 2

    To minimize the impact of insertion and deletion, we can avoid shifting all the elements after the element to be replaced by overwriting the element to be deleted with an arbitrary value or variable. It is best to choose a variable that would not normally be used in the array for easier access when going to insert. Then the insertion function would find the chosen variable using an index and replace it with the required value. This would give the process a complexity of O(1), this making it an optimal process. 

# Questions 3

    Insertion sort:
        insertion sort is possible to apply to a doubly linked list as it works by iterating through a list and iteratively pushing elements into their correct position. Since this method works on the elements of a list one by one, it would not be too difficult of a process to rearrange the pointers so the elements of the linked list become connected in the correct order.  
        
    Merge sort:
        while it is possible to implement merge sort to sort a doubly linked list, it is not very feasible. This is due the the large number of swaps, splitting, and reattaching that occurs in this process. The splitting in each step would mess with the pointers that connect the elements, and the continuous swapping would make it difficult to keep track of the pointers and keep the doubly linked list iterative correctly. 

# Question 4

    Insertion sort:
        The expected complexity of insertion sort is in a linked list O(n^2). One step of an insertion sort in a linked list can have a complexity of O(1) as the step involves simoly rearranging pointers, while in an array is would have a complexity of O(n) due to the need to shift the elements of the array. This names insertion sort more effective in a linked list than in an array. 

    Merge sort:
        The expected complexity of mege sort in a linked list is o(nlogn). Merge sort typically requires extra space to be performed in an array, but in a linked list, it can simply be done by rearranging pointers, thus making it more efficient. 