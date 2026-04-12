class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        U
        input: list of strings
        output: list of lists of strings
        group all anagrams together into these sublists
        use dictionary

        dict = {
            "ath" : ["hat"],
            "act" : ["act", "cat"],
            "opst" : ["stop", "pots", "tops"]
        }

        dict["ath"] = ["hat"]

        strs = ["act","pots","tops","cat","stop","hat"]

        P
        dict = dict()

        for word in words:
            if "".join(sorted(word)) in dict:
                dict["".join(sorted(word))].append(word)
            else:
                dict["".join(sorted(word))] = [word]

        '''

        res = {}

        for word in strs:
            if "".join(sorted(word)) in res:
                res["".join(sorted(word))].append(word)
            else:
                res["".join(sorted(word))] = [word]

        return [value for value in res.values()]