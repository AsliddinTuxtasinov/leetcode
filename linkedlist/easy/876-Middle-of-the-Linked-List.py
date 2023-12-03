"""
Intuition
The intuition for creating a linked list and finding its middle node is straightforward.
We first create a linked list from a given array and then find the middle node of the list.

Approach
1. Define a ListNode class to represent a node in the linked list.
2. Implement an 'append_node' method in the ListNode class to add a new node to the end of the list.
3. Create a linked list from an array using the 'creat_linked_list' function.
4. Extract values from a linked list and return them in a list using the 'get_linked_list_like_list' function.
5. Implement the 'middleNode' method in the Solution class:
   - Convert the linked list to an array using 'get_linked_list_like_list'.
   - Find the index of the middle element in the array.
   - Create a new linked list from the middle to the end of the array using 'creat_linked_list'.
6. The result is the middle node of the original linked list.

Overall, the approach involves using a simple linked list manipulation to create and extract values,
and then applying array operations to find and create the middle portion of the linked list.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append_node(self, val):
        # Intuition: Append a new node with the given value to the end of the linked list.
        new_node = ListNode(val=val)
        current_node = self
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

def creat_linked_list(arr: list) -> Optional[ListNode]:
    # Intuition: Create a linked list from a given array.
    if arr is None:
        return None
    
    head = ListNode(val=arr[0])
    for item in arr[1:]:
        head.append_node(val=item)
    return head

def get_linked_list_like_list(head: ListNode) -> Optional[list]:
    # Intuition: Extract values from a linked list and return them in a list.
    res = []
    if head is None:
        return res
    
    current_node = head
    while current_node.next:
        res.append(current_node.val)
        current_node = current_node.next
    
    res.append(current_node.val)
    return res

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Intuition: Find the middle node of the linked list.
        arr = get_linked_list_like_list(head=head)
        middle_index = len(arr)//2
        return creat_linked_list(arr=arr[middle_index:])



head = creat_linked_list(arr=[1,2,3,4,5,6])
Solution().middleNode(head=head)
