# 234. Palindrome Linked List
# - 연결리스트가 팰린드롬 구조인지 판별하라 (팰린드롬의 정의가 기억나지 않는다면 138p참고)

# 내 답안
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome : List = []

        while head.next :
            palindrome.append(head.val)
            head = head.next
        palindrome.append(head.val)
        
        return palindrome == palindrome[::-1]



#### 책 풀이 - 1. 리스트 반환
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q : List = []
        
        if not head : 
            return true
        
        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 펠린드롬 판별
        while len(q) > 1 :
            if q.pop(0) != q.pop():
                return False
        
        return True


#### 책 풀이 - 2. Deque를 이용한 최적화
# - Deqeu의 명시적인 선언만으로 상당한 속도 개선 효과를 볼 수 있음 (2배 이상)

# 내 풀이의 개선요소
# - 내가 풀이했던 list[::-1]를 이용한 풀이는 n-1개의 요소를 복사하는 것이기 때문에 시간복잡도가 O(N)이 된다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q : Deque = collections.deque()   # list를 Deque로 수정
        
        if not head : 
            return true
        
        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 펠린드롬 판별
        while len(q) > 1 :
            if q.popleft() != q.pop():   # list의 pop(0)대신 popleft()로 변
                return False
        
        return True


#### 책 풀이 - 3. Runner(런너)를 이용한 우아한 풀이
# - Deque로 구현한 풀이와 성능은 비슷하지만, 연결 리스트를 다른 자료형으로 변환하거나 편법을 쓰지 않고 그 자리에서 바로 풀이함

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        
        # Runner를 이용해 역순 연결리스트 구성
        while fast and fast.next :
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            ## Runner의 동작 방식을 보기 위한 코드
            # print("\n-----------------------------------------------")
            # print("fast : ", fast)
            # print("rev : ", rev)
            # print("rev.next : ", rev.next )
            # print("slow : ", slow)
        
        if fast : 
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next 
        return not rev     # rev의 값이 남아있다는 것은 팰린드롬이 성립하지 않았기 때문
