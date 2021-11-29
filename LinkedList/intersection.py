# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA and not headB:
            return None
        
        pa = headA
        pb = headB
        
        while(pa!=pb):
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
            
        return pa
        
#         temp = headA
#         sizeA = 0
#         while(temp):
#             sizeA+=1
#             temp=temp.next
        
#         temp = headB
#         sizeB = 0
#         while(temp):
#             sizeB+=1
#             temp=temp.next
#         diff = sizeB-sizeA
#         flag = 0
#         if(diff>0):
#             flag=1
#             temp = headB
#         elif(diff<0):
#             flag=2
#             temp = headA
#             diff*=-1
#         else:
#             temp = None
#         #Traverse extra nodes in larger list
#         while(temp and diff!=0):
#             temp = temp.next 
#             diff-=1
#         tempA = headA
#         tempB = headB
#         if(flag==1):
#             tempB = temp
#         elif(flag==2):
#             tempA = temp
#         while(tempA and tempB):
#             if(tempA == tempB):
#                 return tempA
#             tempA = tempA.next
#             tempB = tempB.next
#         return None