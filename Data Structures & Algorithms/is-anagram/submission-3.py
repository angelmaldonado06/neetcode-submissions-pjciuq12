from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if len(s) != len(t):
            return False
        
        for key, value in s_counter.items():
            if value != t_counter[key]:
                return False
        
        return True
        