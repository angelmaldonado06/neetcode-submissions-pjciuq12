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
        counter = 0
        newList = list()

        while counter != k: 
            max_key = max(freq, key=freq.get)
            newList.append(max_key)
            del freq[max_key]
            counter += 1
        return newList