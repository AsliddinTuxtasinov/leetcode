"""
Intuition
The problem involves reversing a linked list. One way to solve this is by
traversing the original linked list, storing the values, and then creating
a new linked list with the reversed order of values.

Approach
1. Create a class `ListNode` to represent a node in a singly linked list.
   - Include an `append` method to add a new node to the end of the list.
2. Create a class `Solution` with a method `reverseList`.
3. In the `reverseList` method:
   - Traverse the original linked list and store the values in a list.
   - Reverse the list of values.
   - Create a new linked list with the reversed values.
4. Return the head of the new reversed linked list.

This approach uses a simple list to store values temporarily and then
builds a new linked list with the reversed order of values.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        # ListNode class represents a node in a singly linked list.
        self.val = val  # Value of the node
        self.next = next  # Reference to the next node in the list
    
    def append(self, val):
        # Append a new node with the given value to the end of the list.
        new_node = ListNode(val=val)
        if self.val is None:  # If the current node is empty, set it to the new node.
            self.val = new_node
            return
        
        current_node = self
        while current_node.next:
            current_node = current_node.next  # Traverse the list to find the last node.
        
        current_node.next = new_node  # Add the new node to the end.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            res = []  # Initialize an empty list to store node values.
            current_node = head
            # Traverse the linked list and store the values in the list.
            while current_node.next:
                res.append(current_node.val)
                current_node = current_node.next
            res.append(current_node.val)  # Add the value of the last node.
            res.reverse()  # Reverse the list to get the reversed order of values.

            # Create a new linked list with reversed values.
            new_node = ListNode(val=res[0])
            for item in res[1:]:
                new_node.append(item)

            return new_node  # Return the head of the reversed linked list.
        

# simple array
arr = [1,2,3,4,5]

# create linked list
head = ListNode(val=arr[0])
for item in arr[1:]:
    head.append(item)

reverseList = Solution().reverseList(head=head)
print(reverseList.val)
print(reverseList.next.val)
print(reverseList.next.next.val)
