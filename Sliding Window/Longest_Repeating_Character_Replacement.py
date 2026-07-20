class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        result = 0
        max_value = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_value = max(max_value, count[s[r]])

            while(r - l + 1 - max_value > k):
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        return result