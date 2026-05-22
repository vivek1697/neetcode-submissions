class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        sorted_list = []
        results=[]
        for i in range(len(nums)):
            if nums[i] not in count_hash:
                count_hash[nums[i]]=1
            else:
                count_hash[nums[i]]+=1
        
        sorted_count_hash=dict(sorted(count_hash.items(),key=lambda x: x[1],reverse=True))
        
        sorted_list=list(sorted_count_hash.keys())
        
        for i in range(k):
            results.append(sorted_list[i])
        return results