'''
Understand:
input is an array of intergers
look through the array, and find three elements where they're indices are different that sum up to 0
return a list of all the lists that contain the three elements possible that can sum up to 0
list of lists


Plan:
two pointer
sort                                  i j k
nums = [-1,0,1,2,-1,-4] --> [-4,-1,-1,0,1,2] 
ouput = [[-1,-1,2]]

i = 0,1,2,3
j = 1,2,3,4,5,2,3,4,3,4
k = 5, 4,5

nums[i] = -4,-1, -1, 0
nums[j] = -1,-1,0,1,-1,0,1
nums[k] = 2,1,2
sum = -3,-2,-1,0,-1,2  

-3 < 0 so move middle pointer one index up
-3 < 0 move middle pointer 
-2 < 0          j += 1
-1 < 0          j+= 1

since j = 5 = k, we cant have same index, so we move i+=1, j=i+1, and k last index

0 = 0 so we append the list of the elements at indices i,j,k that make their sum equal to 0,
 we move j up, and k is fixed. check theyre sum, if the sum is large, move k down if its large move j up

-1 < 0, move j up
2 > 0 so we move k down
j = 4 = k, we cant have duplicate indices, so i += 1, (here we check if num[i] == nums[-1] before doing the other pointers) j = i + 1, k = 5 (last index)

we moving i up, we realize that we have the same value as the previous fixed i, so we skip and add i +=1 again.

'''


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        i = 0
        output = []
        #         i     j     k
        #nums = [-4,-1,-1,0,1,2] 
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1



            if i > 0 and nums[i] == nums[i-1]:
                continue
                 

            while j < k:
                sumN = nums[i] + nums[j] + nums[k]
                if(sumN) < 0:
                    j+=1

                elif(sumN) > 0:
                    k-=1
                
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return output






                