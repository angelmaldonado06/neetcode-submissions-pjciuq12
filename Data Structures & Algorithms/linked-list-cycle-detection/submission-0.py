# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
input: a linked list
output: boolean returning true/false if there is is cycle in the linked list

to be considered a cycle, the nodes next pointer points back to previous nodes
two pointer problem (fast and slow)


'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
        
        