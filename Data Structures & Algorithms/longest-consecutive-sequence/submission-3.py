class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_list=sorted(set(nums))
        count = 0
        max_count = -1
        if len(sorted_list) == 1:
            return 1
        
        for i in range(len(sorted_list)-1):
            
            if sorted_list[i] == sorted_list[i+1] - 1:
                count = count + 1
            else:
                count = 0
            max_count=max(max_count,count)
        return max_count +1

        