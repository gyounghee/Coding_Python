# 49. Group Anagrams

# 책 풀이 - 정렬하여 딕셔너리에 추가
## - 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) 
        
        for s in strs:
               anagrams[''.join(sorted(s))].append(s)  
        
        return list(anagrams.values())
