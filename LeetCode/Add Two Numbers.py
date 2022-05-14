class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_n = int(''.join(list(map(str, l1[::-1]))))
        l2_n = int(''.join(list(map(str, l2[::-1]))))
        n_sum = list(str(l1_n+l2_n))
        return list(map(int, n_sum))[::-1]
