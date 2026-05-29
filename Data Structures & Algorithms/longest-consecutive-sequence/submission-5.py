class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        
        setn = set(nums)
        result = 1
        for x in setn:
            temp = x
            length = 1
            while temp+1 in nums:
                length += 1
                temp += 1
                if length > result:
                    result = length


        return result

        

        