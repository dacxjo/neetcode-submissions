class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        sort = sorted(nums)
        temp = sort[0]
        result = 1
        for i in range(1, len(sort)):
            temp += 1
            if temp in sort:
                result +=1
        return result

        

        