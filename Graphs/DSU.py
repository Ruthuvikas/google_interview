class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n1):
            res = n1
            while res != par[n1]:
                res = par[n1]
                par[n1] = par[par[n1]]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        components = n
        for u, v in edges:
            components -= union(u, v)
        return components   

#Time: O(V + E.a)
# Space: O(V)             