class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False

        freq1={}
        freq2={}

        for ch in s:
            freq1[ch]=freq1.get(ch,0)+1
        for ch in t:
            freq2[ch]=freq2.get(ch,0)+1
        return freq1 == freq2    