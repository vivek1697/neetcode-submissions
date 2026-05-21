class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in results:
                return [results[diff], i]
            results[n]=i