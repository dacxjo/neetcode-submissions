class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = float('-inf')
        for k in range(n):
            i = k
            j = n-1
            while i < j:
                area = (j-i) * min(heights[i], heights[j])
                if area > max_area:
                    max_area = area
                if heights[i] < heights[j]:
                    i += 1
                else:
                    j -= 1
            
            

        return max_area
