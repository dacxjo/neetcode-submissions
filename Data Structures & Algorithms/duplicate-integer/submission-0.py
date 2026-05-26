class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1 
                if counter[n] > 1:
                    return True
        return False
        