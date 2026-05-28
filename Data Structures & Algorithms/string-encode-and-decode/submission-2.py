class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for w in strs:
            result += str(len(w)) + "#" + w
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            sep_idx = s.find("#", i)
            length = int(s[i:sep_idx])
            word = s[sep_idx+1 : sep_idx+1+length]
            result.append(word)
            i = sep_idx + 1 + length
        return result
