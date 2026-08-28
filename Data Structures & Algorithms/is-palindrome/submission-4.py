class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        #                                            lr
        #"Was it a car or a cat I saw?" -> "wasitacaroracatisaw" 19 characters
        # tabacat
        '''                        l          r
        s="No lemon, no melon" -> nolemonnomelon
        l = 6, r = 7
        '''


        l,r = 0, len(s)-1

        while l < r:
            if  s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True
