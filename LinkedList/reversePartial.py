# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(not head):
            return head
        if(not head.next):
            return head
        prev = None
        curr = head
        size=1
        while(size!=left):
            prev = curr
            curr = curr.next
            size+=1
        sp = prev
        sc = curr
        tempP,tempC = self.reverse(curr,right-left+1)
        if(sp):
            sp.next = tempP
        else:
            head = tempP
        sc.next = tempC
        return head
        
    def reverse(self,head,size):
        prev = None
        curr = head
        while(size!=0):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            size-=1
        
        return prev,curr
            
        
        