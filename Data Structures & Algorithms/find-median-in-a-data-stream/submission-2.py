class MedianFinder:

    def __init__(self):
        #initilaize an empty array when MedianFinder is called
        self.arr = []

    def addNum(self, num: int) -> None:
        #we add the num to the array
        self.arr.append(num)

    def findMedian(self) -> float:
        #if even, find the mean => the length % 2 == 0: sum(array) / 2
        #else if odd, find the median => round(the length // 2)
        self.arr.sort()

        n = len(self.arr)

        if n % 2 == 0:
            i = n // 2
            return (self.arr[i - 1] + self.arr[i]) / 2
        else:
            return self.arr[n // 2]