class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for num in freq:
            if freq[num]==2:
                ans.append(num)
        return ans
        
        