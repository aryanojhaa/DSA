class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        rev=0
        while x>0:
            digits=x%10
            rev=rev*10+digits
            x=x//10
        if original==rev:
            return True
        else:
            return False
        