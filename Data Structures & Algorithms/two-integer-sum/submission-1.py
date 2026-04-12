class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxDict = dict()

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in idxDict:
                return [idxDict[difference], i]
            else:
                idxDict[nums[i]] = i
