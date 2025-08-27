class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        eq=[]
        large=[]
        for i in nums:
            if i <pivot:
                small.append(i)
            elif i==pivot:
                eq.append(i)
            else:
                large.append(i)
        small.extend(eq)
        small.extend(large)
        return small