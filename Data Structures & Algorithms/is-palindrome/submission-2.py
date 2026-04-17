'''
Understand: 
input a string
make everything to lower case
concatenate all the words
check if it reads the same forward and backward


Plan:

s = "Was it a car or a cat I saw?"

a string variable that keeps the concatenated words
str = ""
for loop that iterates through the characters in s.lower().replace(" ", "")
    we check if the character is a letter 
        str += char
    
done with string variable -> str = "wasitacaroracatisaw"

slicing
reversedStr =st[::-1]

return str == reversedStr
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        s = s.lower().replace(" ", "") # -> s="0p"

        for char in s:
            if char.isalnum():
                st += char

        reversedSt = st[::-1]
        
        return reversedSt == st