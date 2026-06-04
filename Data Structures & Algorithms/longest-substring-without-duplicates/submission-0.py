class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        current_win = set()

        for r in range(len(s)):
            while s[r] in current_win:
                current_win.remove(s[l])
                l += 1

            current_win.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len

            

        