'''
Understand:
max amount of water
two pointer
calcualte area = width * height
find minimum between the two pointers (that will be our height)
find the distance between our two pointers (that will be our width)

            l           r
height = [1,7,2,5,4,7,3,6]
l = 0
r = 7, 6
h = 1
w = 7
max_area = 7

max_area = 0
for l in range(len(height)):
    r = len(height) - 1
        
    while l < r:
        h =  min(height[l], height[r])
        w = r - l
        max_area = max(max_area, h*w)
        r -= 1

max_area = 0
l = 0
r = len(height) - 1

while l < r:
    h =  min(height[l], height[r])
    w = r - l
    max_area = max(max_area, h*w)
    r -= 1
    
    if l == r:
        l+=1
        r = len(height) - 1

'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            h =  min(heights[l], heights[r])
            w = r - l
            max_area = max(max_area, h*w)
            r -= 1
            
            if l == r:
                l+=1
                r = len(heights) - 1

        return max_area



        