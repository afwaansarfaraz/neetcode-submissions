class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        current_sum = 0
        min_length = len(nums) + 1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)

                current_sum -= nums[left]
                left += 1

        if min_length == len(nums) + 1:
            return 0

        return min_length  