class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_a = {}
        count_b = {}

        for i in range(len(s)):
            if s[i] in count_a:
                count_a[s[i]] += 1
            else:
                count_a[s[i]] = 1

        for i in range(len(t)):
            if t[i] in count_b:
                count_b[t[i]] += 1
            else:
                count_b[t[i]] = 1
        
        return count_a == count_b
        

        