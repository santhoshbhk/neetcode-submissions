class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        res = []
        while i < j:
            currSum = numbers[i] + numbers[j]
            if currSum == target:
                res.append(i + 1)
                res.append(j + 1)
                return res
            
            if currSum < target:
                i += 1
            else:
                j -= 1
            
        return []
