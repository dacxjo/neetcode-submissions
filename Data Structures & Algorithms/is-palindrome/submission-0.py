import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = re.sub(r'[^A-Za-z0-9]', '', s)
        cleaned = cleaned.lower()
        left = 0
        right = len(cleaned)-1
        for i in range(0, len(cleaned)):
            if cleaned[left] != cleaned[right]:
                return False
            left +=1
            right -= 1

        return True

        