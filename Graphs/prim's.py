class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjlist[i].append([dist, j])
                adjlist[j].append([dist, i])
        minheap = [(0, 0)]
        visit = set()
        total_distance = 0
        while len(visit) < len(points):
            distance, point = heappop(minheap)
            if point in visit:
                continue
            total_distance += distance
            visit.add(point)
            for dist, neigh in adjlist[point]:
                if neigh not in visit:
                    heappush(minheap, (dist, neigh))
        return total_distance

# Time: O((V + E)logV)
#Space: O(V + E)