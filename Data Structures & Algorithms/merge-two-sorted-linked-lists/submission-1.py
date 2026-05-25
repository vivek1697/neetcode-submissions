# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        sorted_list = []
        current1=list1
        current2=list2
        while current1:
            new_list.append(current1.val)
            current1=current1.next
        
        while current2:
            new_list.append(current2.val)
            current2=current2.next

        sorted_list=sorted(new_list)
        if sorted_list:
            head = ListNode(sorted_list[0])
            current = head

            for element in sorted_list[1:]:
                current.next = ListNode(element)
                current = current.next
            return head 
        else:
            return list1