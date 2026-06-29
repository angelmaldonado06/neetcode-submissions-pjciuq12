class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        index = s.rfind(' ')
        word = s[index+1:]
        return len(word)