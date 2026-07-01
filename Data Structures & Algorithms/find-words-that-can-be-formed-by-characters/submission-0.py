from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        result = 0
        for word in words:
            counter_word = Counter(word)
            is_good = True
            for key, value in counter_word.items():
                if count[key] >= value:  
                    continue
                else:
                    is_good = False
                    break
            if is_good:
                result += len(word)
        return result