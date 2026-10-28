class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1

        while left <= right:
            for i in range(len(nums)):
                if i != left:
                    if nums[left] + nums[i] == target:
                        return [min(left, i), max(left, i)]
            left += 1    
        