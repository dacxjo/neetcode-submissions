class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for item in arr:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        
        sol = []
        for key, value in count.items():
            if value == 1:
                sol.append(key)
        if len(sol) < k:
            return ""
        return sol[k-1]
        