class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        total = 0
        seen = {0: 1}
        for num in nums:
            prefix += num
            if prefix - k in seen:
                total += seen[prefix - k]
            seen[prefix] = seen.get(prefix, 0) + 1
        return total
