class Solution:
    def check(self, nums: List[int]) -> bool:
        original=nums.copy()
        nums.sort()
        for i in range(len(nums)):
            sorted=nums[-i:]+nums[:-i]
            if(sorted==original):
                return True
                break
        else:
            return False
        