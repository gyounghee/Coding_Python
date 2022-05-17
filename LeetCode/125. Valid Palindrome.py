# LeetCode - 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_alnum = [ c for c in s if c.isalpha() or c.isdigit() ]
        return s_alnum == s_alnum[::-1]

#### 책 풀이1 - 리스트로 반환
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for c in s :
            if c.isalnum():    # .isalnum()  →  영문자, 숫자 여부를 판별하는 함수
                strs.append(c.lower())
        
        while len(strs) > 1 :
            if strs.pop(0) != strs.pop() :
                return False
        return True

#### 책 풀이2 - Deque 자료형을 이용한 최적화
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = collections.deque([ c.lower() for c in s if c.isalnum() ])
        
        while len(s_alnum) > 1 :
            if s_alnum.popleft() != s_alnum.pop() :
                return False
        return True

 # 리스트의 pop(0)은 O(N)이지만, Deque의 popleft()는 O(1)이기 때문에 Deque를 이용하는 것이 빠름


#### 책 풀이 3 - 슬라이싱 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)  # 정규식으로 불필요한 문자 필터
        return s == s[::-1]
