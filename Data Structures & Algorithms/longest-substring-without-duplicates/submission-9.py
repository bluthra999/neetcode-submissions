class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        d = dict()

        for right in range(0, len(s)):
            if s[right] in d and d[s[right]]>=left:
                left = d[s[right]]+1
            d[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length



                