class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for w in strs:
            result += str(len(w)) + "#" + w
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        for i in range(0, len(s)):
            if s[i] == "#":
                prev_idx = int(s[i-1])
                word = s[i+1:i+prev_idx+1]
                result.append(word)
        return result
