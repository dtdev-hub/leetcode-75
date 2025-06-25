"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev


# Helpers
def build_linked_list(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert linked_list_to_list(solution.reverseList(build_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(solution.reverseList(build_linked_list([1, 2]))) == [2, 1]
    assert linked_list_to_list(solution.reverseList(build_linked_list([]))) == []

    print("All tests passed.")
