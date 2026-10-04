class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
#not yahan spaces, commas, symbols etc. skip karne ke liye use hua hai.    
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True