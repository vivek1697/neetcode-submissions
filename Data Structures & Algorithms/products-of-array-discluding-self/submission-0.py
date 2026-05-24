class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        new_list=[]
        for i in range(len(nums)):
            total_product=1
            for j in range(len(nums)):
                if i!=j:
                    total_product*=nums[j]
            new_list.append(total_product)
        return new_list
        