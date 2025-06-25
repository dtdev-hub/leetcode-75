"""
LeetCode Helper Functions and Data Structures

This module provides reusable helper functions and basic data structures
for testing and solving LeetCode problems locally.

Currently includes:
- ListNode (singly linked list)
- build_linked_list
- linked_list_to_list

To be extended with:
- TreeNode (binary trees)
- Grid/matrix helpers
- Graph structures
- Priority queue, heap helpers
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    """
    Converts a Python list into a singly linked list.

    Args:
        values (List[int]): List of integers.

    Returns:
        ListNode: Head of the created linked list.
    """
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head

def linked_list_to_list(head):
    """
    Converts a singly linked list back into a Python list.

    Args:
        head (ListNode): Head of the linked list.

    Returns:
        List[int]: Python list of values.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
