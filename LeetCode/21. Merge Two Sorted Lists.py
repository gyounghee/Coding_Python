# 21. Merge Two Sorted Lists
# - 정렬되어 있는 두 연결 리스트를 합쳐라

#### 책 풀이 - 재귀 구조로 연결
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val) :
            list1, list2 = list2, list1
        
        if list1 : 
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1


