# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        size = n
        
        while(curr and curr.next):
            curr = curr.next
            size-=1
            if(size<0):
                prev = prev.next
            elif(size==0):
                prev=head
        if(prev):
            prev.next = prev.next.next
        else:
            return head.next
        return head