class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        U
        input: list of strings
        output: list of lists of strings
        group all anagrams together into these sublists
        use dictionary

        res = {
            "ath" : ["hat"],
            "act" : ["act", "cat"],
            "opst" : ["stop", "pots", "tops"]
        }

        res["ath"] = ["hat"]

        strs = ["act","pots","tops","cat","stop","hat"]

        P
        initialize empty dictionary
        res = {}

        iterate through the list of strings
            if the sorted string is in dictionary:
                append the word to the end of the list where the sorted word was found
            else:
                add the sorted word to the dictionary, and add a list as a value with the word

        '''

        res = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in res:
                res[sortedWord].append(word)
            else:
                res[sortedWord] = [word]

        return list(res.values())