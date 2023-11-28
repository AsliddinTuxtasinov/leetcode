"""
Intuition
We aim to merge two sorted linked lists into a single sorted linked list.

Approach
1. Define a ListNode class to represent each node in the linked list.
2. Implement a function create_linked_list to create a linked list from a given list.
2. Implement a function get_all_nodes_values to extract all values from a linked list.
3. Implement the mergeTwoLists function to merge two linked lists:
    a. Extract values from the input linked lists using get_all_nodes_values.
    b. Merge the values, sort them, and create a new linked list using create_linked_list.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(list: list) -> Optional[ListNode]:
    #  if list is empty, return None
    if list is None or len(list) == 0:
        return None

    # create head Node
    head = ListNode(val=list[0])
    current_node = head

    for val in list[1:]:
        current_node.next = ListNode(val=val)
        current_node = current_node.next
    return head


def get_all_nodes_values(list_node: Optional[ListNode]) -> Optional[list]:
    res = list()

    current_node = list_node
    if list_node is None or list_node == []:
        return res

    while current_node.next:
        res.append(current_node.val)
        current_node = current_node.next

    res.append(current_node.val)
    return res


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    list1 = get_all_nodes_values(list1)
    list2 = get_all_nodes_values(list2)
    return create_linked_list(list=sorted(list1 + list2))


# list1 = create_linked_list(list=[1, 2, 3])
# list2 = create_linked_list(list=[1, 3, 4])

# list1 = create_linked_list(list=[])
# list2 = create_linked_list(list=[])

list1 = create_linked_list(list=[])
list2 = create_linked_list(list=[0])

print(get_all_nodes_values(list_node=mergeTwoLists(list1=list1, list2=list2)))
