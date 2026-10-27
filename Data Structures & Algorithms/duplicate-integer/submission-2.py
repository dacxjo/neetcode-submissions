class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in range(len(nums)):

            if nums[i] in count:
                count[nums[i]] += 1
                if count[nums[i]] == 2:
                    return True
            else:
                count[nums[i]] = 1
        return False