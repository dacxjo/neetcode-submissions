class Solution:

    def threeSumBruteForce(self, nums:List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        seen = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if triplet not in seen:
                            seen.add(triplet)
                            result.append(list(triplet))

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        seen = set()
        sort = sorted(nums)

        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                s = sort[i] + sort[j] + sort[k]
                if s == 0:
                    triplet = (sort[i], sort[j], sort[k]) 
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(list(triplet))
                    j += 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
                

        return result



       