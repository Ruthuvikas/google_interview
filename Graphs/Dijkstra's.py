class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = defaultdict(list)
        for u, v, w in times:
            adjlist[u].append([w, v])
        minheap = [(0, k)]
        distmap = [float('inf')] * (n + 1)
        distmap[k] = 0
        while minheap:
            dist, u = heapq.heappop(minheap)
            for w, v in adjlist[u]:
                if distmap[v] > dist + w:
                    distmap[v] = dist + w
                    heapq.heappush(minheap, (distmap[v], v))
        max_dist = 0
        for node in range(1, n + 1):
            if distmap[node] == float('inf'):
                return -1
            max_dist = max(max_dist, distmap[node])

        return max_dist

# Time: O((V + E)logV)
#Space: O(V + E)