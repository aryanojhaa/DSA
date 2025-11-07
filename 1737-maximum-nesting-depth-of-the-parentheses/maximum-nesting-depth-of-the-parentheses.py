class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        max_length=0
        for ch in s:
            if ch=='(':
                st.append(ch)
                max_length=max(max_length,len(st))
            elif(ch==')'):
                st.pop()
        return max_length
        