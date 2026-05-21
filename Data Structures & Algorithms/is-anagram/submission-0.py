class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash_s = {}
        hash_t = {}
        for value in s:
            if value not in hash_s:
                hash_s[value] = 0
            else:
                hash_s[value] += 1
        
        for value in t:
            if value not in hash_t:
                hash_t[value] = 0
            else:
                hash_t[value] += 1

        return hash_s == hash_t

            
        