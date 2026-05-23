class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_str = ""
        # clean_str="".join(filter(str.isalpha,s)).lower().strip()
        clean_str="".join(char for char in s if char.isalnum()).lower().strip()
        

        for i in range(len(clean_str)):
            reverse_str=clean_str[i]+reverse_str

        print(reverse_str)
        print(clean_str)
        if clean_str == reverse_str:
            return True
        else:
            return False
