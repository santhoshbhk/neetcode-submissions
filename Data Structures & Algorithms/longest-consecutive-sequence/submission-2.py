class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        numSet = set()
        for num in nums:
            numSet.add(num)

        res = 1

        for num in numSet:
            if (num - 1) in numSet:
                continue
            j = num
            tempRes = 1
            while (j + 1) in numSet:
                tempRes += 1
                j += 1
            res = max(tempRes, res)
        
        return res