class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = []
        seen = [False] * len(strs)
        
        for i in range(len(strs)):
            if seen[i]:
                continue
            temp = [strs[i]]
            seen[i] = True
            for j in range(i+1,len(strs)):
                if not seen[j] and sorted(strs[i])==sorted(strs[j]):
                    temp.append(strs[j])
                    seen[j] = True
            results.append(temp)
        return results