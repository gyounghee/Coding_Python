# 5. Longest Palindromic Substring

# 내 풀이
# 길이가 긴 문자열이 들어왔을 때는 시간초과 이슈가 생김
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, s_len = 0, len(s)
        tmp = 0
        while n <= s_len :
            for i in range(n+1):
                if s[i:s_len-tmp+i] == s[i:s_len-tmp+i][::-1] :
                    return s[i:s_len-tmp+i]
            n += 1
            tmp += 1
        return s


#### 책 풀이 - 1. 중앙을 중심으로 확장하는 풀이
#### 난이도 ★★  → 나에겐 좀 어려웠음....ㅜㅜ
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left : int, right : int) -> str :
            while left >= 0 and right < len(s) and s[left] == s[right] :
                left -= 1
                right += 1
            return s[left + 1: right ]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = '' 
        for i in range(len(s) -1 ):
            result = max(result,
                        expand(i, i+1),
                        expand(i, i+2),
                        key = len)
        return result
        
