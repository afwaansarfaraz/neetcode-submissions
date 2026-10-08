class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
             # current no k pehle ka no ni h to ussi no se start hora h tb
            if num - 1 not in seen:
                length = 1

                while num + 1 in seen:
                    num += 1
                    length += 1

                longest = max(longest, length)

        return longest