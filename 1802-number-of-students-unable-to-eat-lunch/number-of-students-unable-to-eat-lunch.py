from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for s in sandwiches:
            if cnt[s] == 0:  
                return cnt[s ^ 1] 
            cnt[s]-=1
        return 0