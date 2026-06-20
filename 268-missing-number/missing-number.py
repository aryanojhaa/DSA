class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=i
        for i in range(len(nums)+1):
            if i not in freq:
                return i
                break
        