'''
                       m
                       l r
Input: nums = [3,4,5,6,1,2], target = 2

if target not in nums:
    return -1

m = (l + r) \\ 2

if nums[m] == target:
    return m

if nums[m] >= nums[l]: 
    if it is, we are on the left side
    we want to determine if target is in between l and m (target < nums[m] and target >= nums[l])
        if it is, we move left
            r = m 
        if it is not, we move right:
            l = m


elif nums[m] < nums[l]:
    we are on the right side
    we want to determine if target is in between m and r (target > nums[m] and target <= nums[r])
        if it is, we move right
            l = m
        if not, move left
            r = m
                     m
                     r   
                     l  
Input: nums = [3,4,5,6,1,2], target = 2
'''

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1