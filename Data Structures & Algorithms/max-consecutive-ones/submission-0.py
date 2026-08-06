class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        temp = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            if i == len(nums)-1:
                max_consecutive = max(max_consecutive, temp) 
            if nums[i] == 0:
                max_consecutive = max(max_consecutive, temp)
                temp = 0
        return max_consecutive
            
        