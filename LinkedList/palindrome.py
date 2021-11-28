# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        size=0
        while(curr and curr.next):
            curr = curr.next.next
            prev = head if prev==None else prev.next
        if(not prev):
            return True
        ns = prev.next
        prev.next = None
        
        #reverse
        prev = None
        curr = ns
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        revStart = prev
        ts = head 
        trs = revStart 
        while(ts and trs):
            if(ts.val!=trs.val):
                return False
            ts =ts.next
            trs = trs.next
        return True
            