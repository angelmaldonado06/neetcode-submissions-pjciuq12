        """
        split the list into 2: [0, 1, 2, 3, 4, 5, 6] HOW????
        l1 = [0, 1, 2, 3]
        l2 = [4, 5, 6]
        How do we know when we are at the middle?
        Two pointer
            fast and slow
            slow moves 1 step at a time while fast 2 steps
            when we reach the end with the fast pointer, that means our slow pointer is at the middle
            slow.next is the head of our second list
            and the middle node now points at null (end of our first list)

        reverse second list
        l2 = [6, 5, 4]

        curr, prev = l2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        prev new reversed l2
        prev = [6, 5, 4]

        append l1 and prev
        first l1 val, then prev val, and so on until empty
         => [0, 6, 1, 5, 2, 4, 3]

        """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        s = slow.next
        slow.next = None

        #slow = [0, 1, 2, 3]
        #l2 = [4, 5, 6]
        #Now reverse l2
        prev = None
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp

        #prev is now our new reversed list
        #prev = [6, 5, 4]

        #append slow = [0, 1, 2, 3] and prev = [6, 5, 4]
        l1 = head
        l2 = prev
        while l1 and l2:
            l1temp = l1.next
            l2temp = l2.next
            l1.next = l2
            l2.next = l1temp

            l1 = l1temp
            l2 = l2temp


        
