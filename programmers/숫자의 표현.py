# 숫자의 표현

def solution(n):
    answer = 0
    nums = [i for i in range(1,n+1)]
    left, right = 0,1
    
    while right != (n+1) :
        if sum(nums[left:right]) == n :
            answer += 1
            right += 1
        elif sum(nums[left:right]) < n :
            right += 1
        elif sum(nums[left:right]) > n :
            left += 1
    return answer

# TEST CASE Ⅰ
n = 15
print(solution(n))   # 4



# 다른 사람 풀이
# - 예를 들어 n이 3개의 연속된 자연수(i-1, i, i+1)의 합으로 표현된다면 합은 3i가 됩니다. 즉, n은 3의 배수입니다.
# - 마찬가지로 5개의 연속된 자연수의 합으로 n이 표현이 된다면 n은 5의 배수여야합니다.
# - 따라서, n의 약수 중 홀수가 몇 개 있냐는 문제와 같은 문제로 해석할 수 있습니다.
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
