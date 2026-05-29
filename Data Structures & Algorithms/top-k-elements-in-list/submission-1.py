class Solution:
    def getCounter(self, nums):
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = nums.count(n)
            else:
                counter[n] += 1
        return counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = self.getCounter(nums)
        print(counter)
        sorted_counter =  {k: v for k, v in sorted(counter.items(), key=lambda item: item[0], reverse=True)}
        return list(sorted_counter.keys())[:k]