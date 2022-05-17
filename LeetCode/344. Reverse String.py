# 344. Reverse String

# ** 제약사항 **
#  - 리턴 없이 리스트 내부를 직접 조작하라

#### 1. 투 포인터를 이용한 스왑
class Solution:
    def reverseString(self, s: List[str]) -> None:
        rp = -1
        for i in range(len(s)//2):
            s[i], s[rp] = s[rp], s[i]
            rp -= 1

#### 2. 파이썬다운 방식
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


# 내 풀이
# s = s[::-1] 을 사용했지만, 이 문제에서는 공간복잡도를 O(1)로 제한하기 때문에 실행되지 않는다.
# 내가 생각한 풀이를 사용하려면 s[:] = s[::-1] 라는 트릭을 이용할 수 있다.
