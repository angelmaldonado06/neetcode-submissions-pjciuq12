"""
U:
we need two pointers representing the left and the right of the window in s
we have to find a substring in s that includes every single character of t, order doesnt matter.

have a count of every character in t to know our limit
min_window we can have it initilized as ""
min_length with the length of s



M:
      l   r
s = "ADOBECODEBANC", t = "ABC"

longest = "ADOBEC"

curr = "DOBEC"
length = 6

first iter:
    l,r = 0,0 -> window 'A'
    is the char that r is pointing at in t? yes
    add 'A' tp substring -> curr = 'A'
    r += 1
second:
    l, r = 0, 1 -> window "AD"
    is the char at r in t? no
    keep going, r += 1

third:
    l, r = 0, 2 -> window 'ADO'
    is O in t? no, keep going
    r+=1
fourth:
    l, r = 0, 3 -> window 'ADOB'
    B in t
    r += 1
fifth: 
    l, r = 0, 4 -> window 'ADOBE'
    E not in t
    r+=1
sixth:
    l, r = 0, 5 -> window 'ADOBEC'
    C in t
    we ran out of our limit
    all characters of t are currenlty in the substring s
    find the length of the the window, compare to current size, if its < than the current min_winwow, replace, else, keep going
    min_length = 6
    min_window = 'ADOBEC'
    l += 1
    r += 1

    so far, we know that our limit of characters in t, is one.
    after adding 1 to l, we check the character that we deleted from our winwow, check if it is one on the chars in t, and in this case we left A out, we go back to finding another A so we can satisify our limit.

seventh: 
    l,r = 1,6 -> window 'DOBECO'


tcount = Counter(t) -> {'A' : 1, 'B' : 1, 'C' : 1}
window_count = {}

"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = Counter(t)
        window_count = {}

        have = 0
        need = len(t_count)

        l = 0
        res = ""
        res_len = float("inf")

        for r in range(len(s)):
            char = s[r]
            
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                if(r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                window_count[s[l]] -= 1

                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l+= 1

        return res

        