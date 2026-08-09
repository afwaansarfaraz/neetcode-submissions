class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d ={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                    d[num]+=1
        Topk = sorted(d , key=d.get , reverse = True)[:k]
        return Topk              