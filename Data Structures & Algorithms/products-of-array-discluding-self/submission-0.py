class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        countOfZeros = 0
        for num in nums:
            if num == 0:
                countOfZeros += 1
            else: 
                total *= num
        
        res = []

        if countOfZeros > 1:
            res = [0 for i in range(len(nums))]
            return res

        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(total)
            elif countOfZeros > 0:
                res.append(0)
            else:
                res.append(total // nums[i])

        return res