class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        for loop:
            maxx = arr[i]
            for loop: starts at i + 1
                we find the max number to the right of arr[i]
                maxx = max(arr[j], maxx)
            arr[i] = maxx
        
        '''
        n = len(arr)
        for i in range(n):
            maxx = arr[i+1] if i < n - 1 else arr[i]
            for j in range(i+1, len(arr), 1):
                maxx = max(arr[j], maxx)
            arr[i] = maxx
        arr[-1] = -1
        return arr