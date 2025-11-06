class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for ch in operations:
            if ch not in ['C', 'D', '+']:
                st.append(int(ch))
            elif ch == 'C':
                st.pop()
            elif ch == 'D':
                st.append(2 * st[-1])
            elif ch == '+':
                st.append(st[-1] + st[-2])
        return sum(st)
