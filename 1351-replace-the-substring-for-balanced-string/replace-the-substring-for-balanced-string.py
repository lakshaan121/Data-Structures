from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        dict1 = Counter(s)
        left = 0
        n = len(s)
        needed = n // 4
        min_len = n
        for right in range(n):
            dict1[s[right]] -= 1
            while left<n and (dict1['Q'] <= needed and
                   dict1['W'] <= needed and
                   dict1['E'] <= needed and
                   dict1['R'] <= needed):
                min_len = min(min_len, right - left + 1)
                dict1[s[left]] += 1
                left += 1
        return min_len