"""234. Palindrome Linked List
Intuition
The problem involves determining whether a linked list is a palindrome,
meaning it reads the same forward as backward. One intuitive approach is to convert 
the values of the linked list nodes into a string and check if that string is a palindrome.

Approach
The script initializes an empty string (res) and starts traversing the linked list from the head. 
It concatenates the values of each node to the string. After traversing the entire linked list,
the script compares the string with its reverse to check for palindrome property. 
The approach assumes that ListNode is a class representing a node in a linked list.
While this approach is straightforward, it has a space complexity of O(n), where n is the length of the linked list, 
due to the use of the string res. There may be more memory-efficient approaches, 
such as using two pointers to find the middle of the linked list and then reversing the second half for comparison.link
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Check if the linked list is empty
        if head is None:
            return False
        
        # Initialize an empty string to store the values of the linked list
        res = ""
        
        # Start from the head of the linked list
        current_node = head
        
        # Traverse the linked list and concatenate the values to the string
        while current_node.next:
            res += str(current_node.val)
            current_node = current_node.next
        
        # Add the value of the last node to the string
        res += str(current_node.val)
        
        # Check if the string is equal to its reverse, indicating a palindrome
        return res == res[::-1]
