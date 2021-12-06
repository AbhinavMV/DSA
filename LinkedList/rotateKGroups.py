# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right=head
        n = k
        if(k==1 or not head):
            return head
        while(right and n!=0):
            right=right.next
            n-=1
        h,l = self.reverseLL(head,k)
        head = h
        left=right
        n=k
        while(right):
            right=right.next
            n-=1
            if(n==0):
                temp = right
                nh,nl = self.reverseLL(left,k)
                l.next=nh
                h=nh
                l=nl
                n=k
                left=temp
        if(n>0):
            l.next=left
        return head
        
    def reverseLL(self,head,k):
        prev=None
        curr=head
        while(curr and k!=0):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            k-=1
        return prev,head
        