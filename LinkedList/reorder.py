# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #get mid
        prev = curr = head
        while(curr and curr.next):
            curr = curr.next.next
            prev = prev.next
        #reverse after middle
        temp = prev
        prev = None
        curr = temp
        while(curr):
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        #rearrange
        listA = head
        listB = prev
        final = None
        while(listB):
            final = listB
            tA = listA.next if listA else None
            if listA:
                listA.next = listB
            listA = tA
            tB = listB.next
            listB.next = listA
            listB = tB
        final.next = None