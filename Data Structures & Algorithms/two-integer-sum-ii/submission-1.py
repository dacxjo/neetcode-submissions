class Solution:
    def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:

        result = []
        # O(n^2)
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i < j:
                    if numbers[i] + numbers[j] == target:
                        result.append(i+1)
                        result.append(j+1)
                        break
        return result
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
        