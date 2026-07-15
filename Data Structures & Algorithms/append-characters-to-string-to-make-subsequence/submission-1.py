class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        pt = 0
        for ch in s:
            if pt < len(t) and ch == t[pt]:
                pt += 1
        return len(t) - pt