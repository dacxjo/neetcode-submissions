class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        sort = sorted(nums)
        result = 0
        for i in range(0, len(nums)-1):
            if sort[i]+1 == sort[i+1] or sort[i] == sort[i+1]:
                result += 1
        return result

        