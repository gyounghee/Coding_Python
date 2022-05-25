# 2. Add Two Numbers
# - 역순으로 저장된 연결 리스트의 숫자를 더하라.

# 내 답안 - 실패
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node, l2_node = l1, l2
        prev = ListNode()
        plus = 0
        
        while l1_node or l2_node or plus: 
            add_n = list(str(l1_node.val + l2_node.val + plus))
            
            if len(add_n) > 1 :
                plus = int(add_n[0])
                add_nums = int(add_n[1])
            else :
                add_nums = add_n[0]
                plus = 0
            
            sum_node, sum_node.next = prev, add_nums
            prev = sum_node
            l1_node, l2_node = l1_node.next, l2_node.next
        
        return prev


#### 책 풀이 - 1. 자료형 변환
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 연결 리스트 뒤집기
        def reverseList(self, head) -> ListNode :
            node, prev = head, None
            
            while node :
                next_node, node.next = node.next, prev
                prev, node = node, next_node
            
            return prev
        
        # 연결 리스트를 파이썬 리스트로 변환
        def toList(self, node) -> ListNode :
            lst = []
            while node :
                lst.append(node.val)
                node = node.next
            
            return lst
        
        # 파이썬 리스트를 연결리스트로 변환
        def toReverseLinkedList(self, result) -> ListNode :
            prev = None
            for r in result :
                node = ListNode(r)
                node.next = prev
                prev = node
            
            return node
        
        # 두 연결 리스트의 덧셈
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            a = self.toList(self.reverseList(l1))
            b = self.toList(self.reverseList(l2))

            resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
            
            # 최종 결과 연결리스트 변환
            return self.toReverseLinkedList(str(resultStr))


#### 책 풀이 - 2. 전가산기 구현
        class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        
        carry = 0 
        while l1 or l2 or carry :
            sum = 0
            # 두 입력값의 합 계산
            if l1 :
                sum += l1.val
                l1 = l1.next
            if l2 :
                sum += l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next
    
