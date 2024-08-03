class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for neigh in adjlist[node]:
                if neigh == par:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visit) == n

#Time: O(V + E)
#Space: O(V + E)

#Note
# ensure the graph is fully connected and also there is no cycles in the graphs, when we check for cycles 
# we need to avoid checking trivial cycles like A->B->A.
