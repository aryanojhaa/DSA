class Solution:
    def largestOddNumber(self, num: str) -> str:
        s=num
        lst=[]
        for i in range(len(s)):
            x=s[i]
            lst.append(x)
        y=list(map(int,lst))
        for j in range(len(y) - 1, -1, -1):
            if y[j] % 2 != 0:
                return "".join(lst[:j+1])
        return ""
        
      
        
        