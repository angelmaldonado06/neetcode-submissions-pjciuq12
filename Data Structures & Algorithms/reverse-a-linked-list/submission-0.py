'''
input: head = [0,1,2,3]
head -> 0 -> 1 -> 2 -> 3 -> Null
head -> 3 -> 2 -> 1 -> 0 -> Null


recursively
Base Case: when a node next pointer is null
recursive step: reverse the rest of the list after the current node
head.next.next = head
head.next = null
return: the new head 

'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        dummy = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return dummy
        