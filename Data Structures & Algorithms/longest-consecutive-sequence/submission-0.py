'''
for loop that iterates nums

    Input: nums = [2,20,4,10,3,4,5]
    nums = set(nums) = (2,20,4,10,3,5) --->    2,3,4,5    20     10

    for loop range(len(nums)):
        if element has no left neighbor: if element-1 not in nums
            starting sequence
            while starting sequence has right neighbor:
                we add 1 to the length
        check which length is loger
    return length

length = 1,2,3,4
curr = 2, 3,4,5,6

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_length = 0
        
        for n in unique_nums:
            if (n-1) not in unique_nums:
                curr = n
                length = 0

                while curr in unique_nums:
                    length += 1
                    curr += 1
                max_length = max(length, max_length)

        return max_length

