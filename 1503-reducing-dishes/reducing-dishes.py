#GREEDY APPROACH
from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = 0
        result = 0
        for s in satisfaction:
            total += s
            if total > 0:
                result += total
            else:
                break
        return result