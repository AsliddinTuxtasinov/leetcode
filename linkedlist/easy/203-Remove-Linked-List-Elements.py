from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def creat_linked_list(arr: list) -> ListNode:
    # Create a linked list from an array
    if len(arr) == 0:
        return
    
    # Initialize the head of the linked list
    head = ListNode(val=arr[0])
    current_node = head
    
    # Iterate through the array and create linked list nodes
    for item in arr[1:]:
        current_node.next = ListNode(val=item)
        current_node = current_node.next
    
    return head

        
# Class for the solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Check if the linked list is empty
        if head is None:
            return
        
        # Initialize an empty array and start from the head of the linked list
        arr, current_node = [], head
        
        # Traverse the linked list and append non-matching values to the array
        while current_node.next:
            if current_node.val != val:
                arr.append(current_node.val)
            current_node = current_node.next
        
        # Append the value of the last node if it does not match the target value
        if current_node.val != val:
            arr.append(current_node.val)
        
        # Create a new linked list from the filtered array of values
        return creat_linked_list(arr=arr)


head = creat_linked_list(arr=[1,2,6,3,4,5,6])
Solution().removeElements(head=head, val=6)
