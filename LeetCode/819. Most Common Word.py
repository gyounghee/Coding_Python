# 819. Most Common Word

## 내 풀이
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^A-Za-z0-9 ]',' ',paragraph).lower()
        
        words = [c for c in paragraph.split() if c.isalpha() ]
        word_dic = collections.Counter(words)
        
        for b in banned:
            del word_dic[b]
        
        max_c = 0
        
        for k, v in word_dic.items() :
            if v >= max_c :
                w, max_c = k, v
        return w


## 책 풀이 - 리스트 컴프리헨션(List Comprehension), Counter 객체 사
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = collections.defaultdict(int)
        for word in words :
            counts[word] += 1
        
        return max(counts, key=counts.get)



## 책 풀이 참고하여 내 풀이 보완
# Conter 객체의 빈도수가 높은 요소를 찾는 most_common() 사용
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^A-Za-z0-9 ]',' ',paragraph).lower()
        
        words = [c for c in paragraph.split() if c.isalpha() ]
        word_dic = collections.Counter(words)
        
        for b in banned:
            del word_dic[b]
        
        return word_dic.most_common(1)[0][0]  # most_common(숫자)  : Counter 객체에서 가장 빈도 수가 높은 요소 추출하는 방법
