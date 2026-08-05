class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        revFreq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            freq[i] += 1
        
        for key in freq:
            revFreq[freq[key]].append(key)

        res = []

        for i in range(len(revFreq) - 1, 0, -1):
            if len(revFreq[i]) == 0:
                continue
            
            for j in range(len(revFreq[i])):
                res.append(revFreq[i][j])
            if len(res) == k:
                return res
        
        
        

