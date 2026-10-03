class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0 
        j = 0
        window = set()
        for j in range(len(nums)):
            if j - i > k :
                window.remove(nums[i])
                i+=1
            if nums[j] in window:
                return True
            window.add(nums[j])
        return False            