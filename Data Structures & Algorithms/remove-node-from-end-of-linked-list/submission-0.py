# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []

        while head:
            l.append(head.val)
            head = head.next
    
        count = 1
        for i in range(len(l), 0, -1):
            if count == n:
                l.pop(i-1)
            count += 1
        
        if not l:
            return None

        new_list = ListNode(l[0])
        current = new_list
    
        for i in range(1, len(l)):
            current.next = ListNode(l[i])
            current = current.next
        return new_list

