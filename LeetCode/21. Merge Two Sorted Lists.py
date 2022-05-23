# 21. Merge Two Sorted Lists
# - 정렬되어 있는 두 연결 리스트를 합쳐라

#### 책 풀이 - 1. 재귀 구조로 연결
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1이 존재하지 않거나 또는 list2가 존재하면서 list1의 첫 번쨰 값이 list2의 첫 번째 값보다 크면
        if (not list1) or (list2 and list1.val > list2.val) :
            list1, list2 = list2, list1    # 항상 list1에 작은 값이 들어가도록 swap(스왑)
        
        if list1 :  # list1이 존재하면 
            # list1.next는 list1.next의 다음 원소와 list2의 값을 파라미터로 하여 재귀
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1  


#### 책 풀이 - 2. 반복 구조로 뒤집기
class ListNode :
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node :
            next_node, node.next = node.next, prev
            prev , node = node, next_node
            
        return prev
            
