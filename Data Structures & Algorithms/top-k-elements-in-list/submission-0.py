import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        fmap ={}
        for i in nums:
            fmap[i] = 1 + fmap.get(i,0)
        for i,c in fmap.items():
            freq[c].append(i)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

        