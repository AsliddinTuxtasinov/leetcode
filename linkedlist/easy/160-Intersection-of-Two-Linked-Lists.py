# from typing import Optional
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def getIntersectionNode(self, head_A: ListNode, head_B: ListNode) -> Optional[ListNode]:
#         list_a = []
#         list_b = []
#
#         current_node = head_A
#         while current_node.next:
#             list_a.append(current_node.val)
#             current_node = current_node.next
#         list_a.append(current_node.val)
#
#         current_node = head_B
#         while current_node.next:
#             list_b.append(current_node.val)
#             current_node = current_node.next
#         list_b.append(current_node.val)
#
#         len_range = len(list_b) if len(list_a) > len(list_b) else len(list_a)
#
#         res = [
#                   list_a[::-1][i]
#                   for i in range(len_range)
#                   if (list_a[::-1][i] == list_b[::-1][i]) and
#                      (list_a[::-1][i] != 1)
#               ][::-1]
#
#         if len(res) == 0:
#             return None
#         return ListNode(x=res[0])
#
#
# if __name__ == '__main__':
#     listA = [1, 9, 1, 2, 4]
#     listB = [3, 2, 4]
#
#     headA = ListNode(listA[0])
#     current_head = headA
#     for a in listA[1:]:
#         current_head.next = ListNode(a)
#         current_head = current_head.next
#
#     headB = ListNode(listB[0])
#     current_head = headB
#     for b in listB[1:]:
#         current_head.next = ListNode(b)
#         current_head = current_head.next
#
#     Solution().getIntersectionNode(head_A=headA, head_B=headB)
