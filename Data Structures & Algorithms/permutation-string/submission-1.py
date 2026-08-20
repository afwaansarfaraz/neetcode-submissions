class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        d1 = {}
        d2 = {}

        for ch in s1:
            d1[ch] = d1.get(ch, 0) + 1

        for r in range(len(s2)):
            d2[s2[r]] = d2.get(s2[r], 0) + 1

            if r - l + 1 == len(s1):

                if d1 == d2:
                    return True

                d2[s2[l]] -= 1

                if d2[s2[l]] == 0:
                    del d2[s2[l]]

                l += 1

        return False