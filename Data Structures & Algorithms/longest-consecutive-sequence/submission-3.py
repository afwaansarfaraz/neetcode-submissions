class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                length = 1

                while num + 1 in seen:
                    num += 1
                    length += 1

                longest = max(longest, length)

        return longest