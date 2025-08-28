class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        x=lst[::-1]
        y=' '.join(x)
        return y
        