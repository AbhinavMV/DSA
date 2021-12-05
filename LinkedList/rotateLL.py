# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head):
            return head
        temp = head
        size = 0
        while(temp):
            size+=1
            temp=temp.next
        diff = k%size
        if(diff==0): 
            return head
        prev=head
        curr=head
        while(curr.next):
            curr=curr.next
            if(diff<=0):
                prev=prev.next
            diff-=1
        temp = prev.next if prev else None
        if prev:
            prev.next=None 
            curr.next=head
            head=temp
        return head

#         while(k>0):
#             node = self.deleteEnd(head)
#             h = self.insertBegin(head,node)
#             head = h
#             k-=1
#         return head
        
#     def deleteEnd(self,node):
#         prev = None
#         curr = node
#         while(curr.next):
#             prev = curr
#             curr = curr.next
#         prev.next = None
#         return curr
    
#     def insertBegin(self,head,node):
#         node.next = head
#         head = node
#         return head