class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''


        hashmap = {
            "act"=["act"],
            "opst"=["pots", "tops"]

        
        
        }
        for s in strs:
            s_copy = "".join(sorted(s)) -> act, opst
            if s_copy not in the hashmap
                add it
                hashmap[s_copy] = [s]
            elif s_copy IN hashmap:
                hashmap[s_copy].append(s)
    
        return [x for value in hashmap.values()]
        
        '''

        hashmap = {}

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted not in hashmap:
                hashmap[s_sorted] = [s]
            else:
                hashmap[s_sorted].append(s)

        return [x for x in hashmap.values()]
        