class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        seen[nums[0]] = 0

        for i in range(1, len(nums)):
            look = target - nums[i]
            if look in seen:
                return [seen[look], i]
            else:
                seen[nums[i]] = i