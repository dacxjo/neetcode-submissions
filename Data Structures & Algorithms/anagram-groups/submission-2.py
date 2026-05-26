class Solution:

    def make_counter(self, s):
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        return frozenset(counter.items())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        result = []
        for s in strs:
            counter = self.make_counter(s)
            if counter not in result_dict:
                result_dict[counter] = [s]
            else: 
                result_dict[counter].append(s)
        return list(result_dict.values())