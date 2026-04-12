from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = Counter(nums)

        for key, value in x.items():
            if value > 1:
                return True
        return False
        