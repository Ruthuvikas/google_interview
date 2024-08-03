class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[src] = 0
        for i in range(k + 1):
            tmp = dp[:]
            for frm, to, price in flights:
                if dp[frm] == float('inf'):
                    continue
                if dp[frm] + price < tmp[to]:
                    tmp[to] = dp[frm] + price
            dp = tmp
        return dp[dst] if dp[dst] != float('inf') else -1

#Time: O(V.E)
#Space: O(V)