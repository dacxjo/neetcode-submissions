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

        result = []
        pointer = 0
        # O(n)
        for i in range(len(numbers)):
            while pointer < len(numbers):
                if i < pointer:
                    if numbers[i] + numbers[pointer] == target:
                        result.append(i+1)
                        result.append(pointer+1)
                        break
                pointer += 1
            pointer = 0

        return result
        