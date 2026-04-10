class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # take two strings S and T and return true if the two strings are anagrams otherwise return false
        # Order of characters can be different but they contain exact same characters