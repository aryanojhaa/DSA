class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        n=len(edges)+1
        adj = [[] for i in range(n+1)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        for i in range(1,n+1):
            if len(adj[i])==n-1:
                return i