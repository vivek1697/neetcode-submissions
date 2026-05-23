class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str="".join(char for char in s if char.isalnum()).lower().strip()
        i = 0
        j = len(clean_str)-1
        if clean_str is None:
            return True
        for _ in range(int(len(clean_str)/2)):
            if clean_str[i]==clean_str[j]:
                i += 1
                j -= 1
            else:
                return False
        return True