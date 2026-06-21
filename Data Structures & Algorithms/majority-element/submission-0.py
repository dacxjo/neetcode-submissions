class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        
        majority = len(nums) // 2
        result = None
        for key, value in count.items():
            if value > majority:
                result = key
        return result