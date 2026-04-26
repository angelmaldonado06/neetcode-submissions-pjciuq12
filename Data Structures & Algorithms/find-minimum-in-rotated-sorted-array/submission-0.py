'''
              r 
              l   
nums = [3,4,5,6,1,2]

l = 0,3
r = len(nums) - 1, 4
res = nums[0],5,1


while l < r:

    m = (r + l)//2 -> 2,4,3,4,1
    res = min(res, nums[m])
    if nums[m] greater than or equal l:
        move right
        l = m + 1
    else:
        move left (meaning that we are on the right side)
        r = m - 1
    
'''



class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r =0,len(nums)-1
        res = nums[0]

        while l <= r:
            m = (l + r)//2
            res = min(res,nums[m])

            if nums[m] >= nums[l]:
                l += 1
            else:
                r = m - 1

        return res

        
        
        