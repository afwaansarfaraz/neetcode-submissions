class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        max_freq = 0
        longest = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1

            max_freq = max(max_freq, d[s[r]])

            #current window me kitne characters hain.
            while (r - l + 1) - max_freq > k:
        
                d[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest