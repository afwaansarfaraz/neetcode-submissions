class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while r - l + 1 > k:
            if abs(x - arr[l]) > abs(x - arr[r]):
                l += 1
            else:
                r -= 1

        return arr[l:r+1]