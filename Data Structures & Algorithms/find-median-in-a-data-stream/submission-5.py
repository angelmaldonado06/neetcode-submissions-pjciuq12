# class MedianFinder:

#     def __init__(self):
#         #initilaize an empty array when MedianFinder is called
#         self.arr = []

#     def addNum(self, num: int) -> None:
#         #we add the num to the array
#         self.arr.append(num)

#     def findMedian(self) -> float:
#         #if even, find the mean => the length % 2 == 0: sum(array) / 2
#         #else if odd, find the median => round(the length // 2)
#         self.arr.sort()

#         n = len(self.arr)

#         if n % 2 == 0:
#             i = n // 2
#             return (self.arr[i - 1] + self.arr[i]) / 2
#         else:
#             return self.arr[n // 2]

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        # if(self.small and self.large and (-1 * self.small[0]) > self.large[0]):
        #     val = -1*heapq.heappop(self.small)
        #     heapq.heappush(self.large,val)

        # #if uneven size
        # if(len(self.small) > len(self.large) + 1):
        #     val = -1* heapq.heappop(self.small)
        #     heapq.heappush(self.large,val)
        # if(len(self.large) > len(self.small) + 1):
        #     val = heapq.heappop(self.large)
        #     heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        # if len(self.small) > len(self.large):
        #     return -1 * self.small[0]
        # if len(self.large) > len(self.small):
        #     return self.large[0]

        # return (-1 * self.small[0] + self.large[0]) / 2
        if self.small and len(self.small) != len(self.large):
            return -self.small[0]
        elif self.small and self.large:
            return (-self.small[0] + self.large[0]) / 2
