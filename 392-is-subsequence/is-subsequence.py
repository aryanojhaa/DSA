class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        new = ""
        for ch in range(len(t)):
            if len(new)<len(s) and t[ch] == s[len(new)]:
                new += t[ch]
        if s == new:
            return True
        else:
            return False
