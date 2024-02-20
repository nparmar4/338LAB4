# Provided Implementation
def reverse(self):
    newhead = None
    prevNode = None
    for i in range(self.get_size()-1, -1, -1):
        currNode = self.get_element_at_pos(i)
        currNewNode = Node(currNode.data)
        if newhead is None:
            newhead = currNewNode
        else:
            prevNode.next = currNewNode
        prevNode = currNewNode
    self.head = newhead

# 2: Optimized Function
def reverse_optimized(self):
    prev_node = None
    current_node = self.head

    while current_node:
        next_node = current_node.next  
        current_node.next = prev_node  
        prev_node = current_node  
        current_node = next_node  

    self.head = prev_node  
# Code Referenced from ChatGPT
    
