class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in prerequisites:
            adjlist[v].append(u)
            indegree[u] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        course = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                course += 1
                for neigh in adjlist[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue.append(neigh)
        return course == numCourses

#Time: O(V + E)
#Space: O(V + E)