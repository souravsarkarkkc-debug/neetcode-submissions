"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr is not None:
            copied = Node(curr.val)
            copied.next = curr.next
            curr.next = copied
            curr = copied.next

        curr = head
        while curr is not None:
            copied = curr.next
            if curr.random is not None:
                copied.random = curr.random.next

            curr = copied.next

        if head is None:
            return None
        new_head = head.next
        curr = head
        while curr is not None:
            copied = curr.next
            curr.next = copied.next
            if curr.next is not None:
                copied.next = curr.next.next
            else:
                copied.next = None

            curr = curr.next
        return new_head
        