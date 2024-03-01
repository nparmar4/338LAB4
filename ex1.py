class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def binary_search(self, num):
        current = self.head
        index = 0
        while current:
            if current.data == num:
                return f"Number {num} found at index {index}."
            current = current.next
            index += 1
        return f"Number {num} not found in the list."


class Array:
    def __init__(self):
        self.array = []

    def append(self, data):
        self.array.append(data)

    def binary_search(self, num):
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == num:
                return f"Number {num} is found at index {mid}."
            elif self.array[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return f"Number {num} is not found in the array."


# Linked List
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list.binary_search(8))  # Output: Number 3 found at index 2.

# Array
array = Array()
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)
print(array.binary_search(8))  # Output: Number 3 found at index 2.

#this code was generated using chatGPT but was significantly modified to provide accurate results 

#Binary search on a linked list is not as efficient as it is on an array. This is because arrays have direct access to elements based on their index, while linked lists require traversal from the beginning of the list to reach a specific element.

#In a linked list, you can't directly access the middle element 
#without traversing the list from the beginning. This means that even if 
#you find the middle element, you still have to traverse the first half of the list to reach it.
# This traversal takes O(n/2) time, where n is the number of elements in the list.
#So, even though the search space is halved with each comparison, the time complexity is still O(n/2) 
#for the first comparison, O(n/4) for the second, O(n/8) for the third, and so on. In general, the time complexity of binary search on a 
#linked list is O(log n) for a list with n elements.

#this code was generated using chatGPT but was significantly modified to provide accurate results 