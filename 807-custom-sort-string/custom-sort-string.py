from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict1 = dict(Counter(s))
        dict2 = dict(Counter(order))
        rem = ""
        for ch in s:
            if ch not in dict2:
                rem += ch
        prefix = ""
        for ch in order:
            if ch in dict1:
                prefix += ch * dict1[ch]
        return prefix + rem