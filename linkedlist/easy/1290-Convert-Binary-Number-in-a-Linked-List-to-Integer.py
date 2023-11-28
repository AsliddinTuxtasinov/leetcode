"""
Intuition
The problem involves converting a binary linked list to its decimal representation.
One way to approach this is to traverse the linked list, collect the binary digits,
and then calculate the decimal value.

Approach
Create a function to get all values from the linked list and return them as a list.
In the Solution class, use the get_all_nodes_values function to get the binary digits,
reverse the list to process it from LSB to MSB, and then calculate the decimal value.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr: list) -> ListNode:
    if arr is None:
        return None
    
    head = ListNode(val=arr[0])
    
    current_node = head
    for val in arr[1:]:
        current_node.next = ListNode(val=val)
        current_node = current_node.next

    return head

# Function to get all values from the linked list
def get_all_nodes_values(linked_list: ListNode) -> Optional[list]:
    res = []
    if linked_list is None:
        return res
    
    current_node = linked_list
    # Traverse the linked list and append values to the result list
    while current_node.next:
        res.append(current_node.val)
        current_node = current_node.next
    
    # Append the value of the last node
    res.append(current_node.val)
    return res


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Get the values of all nodes in the linked list
        arr = get_all_nodes_values(linked_list=head)
        # Reverse the list to process it from LSB to MSB
        arr.reverse()
        
        res = 0
        # Calculate the decimal value using the reversed list
        for index in range(len(arr)):
            res = res + arr[index] * (2**index) 
        return res


head = create_linked_list(arr=[1,0,1])
# head = create_linked_list(arr=[0])

print(Solution().getDecimalValue(head=head))
