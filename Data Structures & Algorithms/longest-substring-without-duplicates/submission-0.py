'''
understand:
two pointers - one slow, one fast
first pointer will keep track of the begging of substring, second will be the end
if the fast pointer happends to point to a char that is already in the window, then end of substring
find length eveytime we move right pointer, and check if its greater than max_length

left, right = 0, 1

 l  r
zxyzdfgh

      l  r
s = "zxyzxyz"

l=0
r=1,2
z in substring? no
substring = z
length? 1
add 1 to r
x alreay in substring? no keep going
substring = zx
length = 2
add 1 to 
y in substring? no add the char to substring 
s[l:r] --> zxy
sustring = zxy
length = 3
add 1 to r
z in substring? yes
add 1 to l and r
x in substring?
add 1 to l and r
y in substring?
add 1 to l and r
z in substring?
add 1



substring = xyz

max_length

while loop that check whether r <= len(s)
    if the curent char is not already in the substring: (current char is the one at index r - 1)
        substring += char
        max_length = max(max_length, len(substring))
        r += 1
    else if its in the substring:
        l+=1
        r+=1

    

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length
        