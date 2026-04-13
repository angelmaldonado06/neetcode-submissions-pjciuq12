from collections import Counter



'''
freq = {
    1 : 1,
    2 : 2,
    3 : 3,
}

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        
        return [x for x, y in freq.most_common(k)]