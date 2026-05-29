class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for w in strs:
            result += str(len(w)) + "#" + w
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        for i in range(0, len(s)):
            if s[i].isnumeric():
                length = int(s[i])
                sep_idx = i+1
                word = s[sep_idx+1:sep_idx+length+1]
                result.append(word)
        return result
