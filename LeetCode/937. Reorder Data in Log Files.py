# 937. Reorder Data in Log Files

# 로그를 재정렬하라.
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha, digit = [], []  #  문자로 구성된 로그, 숫자로 구성된 로그를 따로 담을 수 있는 list 생성
        for i in range(len(logs)) :
            if logs[i].split()[1].isdigit() :   
                digit.append(logs[i])
            else : 
                alpha.append(logs[i])
        
        alpha.sort(key = lambda x : (x.split()[1:], x.split()[0]))  # 식별자를 제외한 문자열로 정렬하고 같다면 식별자로 정렬하도록
        
        return alpha + digit
