class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sub = nums[0]
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sub = max(max_sub, cur_sum)
        return max_sub