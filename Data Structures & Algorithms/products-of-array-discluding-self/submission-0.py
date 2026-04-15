"""
output = []
while loop that keeps track of every element (moves slow) i
    while the element is not the same as the outer loop i != j
        output.append(i*j)

return output

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        '''

        nums = [1,2,4,6]
        i = 0, 1
        j = 0,1,2,3,4
        product = 1, 1,4, 24

        '''
        for i in range(len(nums)):
            j = 0
            product = 1
            while j < len(nums):
                if i != j:
                    product *= nums[j]
                j += 1
            output.append(product)

        return output