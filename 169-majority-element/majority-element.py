class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        n=len(nums)
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i],0)+1
            if freq[nums[i]] > (n/2):
                return nums[i]
        