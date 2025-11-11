class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=int(''.join(map(str,digits)))
        x=x+1
        lst=list(map(int,str(x)))
        return lst