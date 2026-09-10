# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1=ListNode(0)
        ans=dummy1
        temp=head
        while temp :
            if temp.next and temp.val==temp.next.val:
                while temp.next and temp.next.val==temp.val:
                    temp=temp.next
                temp=temp.next
            else:
                dummy1.next=ListNode(temp.val)
                temp=temp.next
                dummy1=dummy1.next
        return ans.next



            
            