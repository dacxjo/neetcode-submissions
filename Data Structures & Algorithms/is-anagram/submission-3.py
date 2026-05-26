class Solution:

    def get_count(self, s):
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        return counter

    
    def isAnagram(self, s: str, t: str) -> bool:
        counter = self.get_count(s)
        counter_2 = self.get_count(t)

        return counter == counter_2
        
        