
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        current_adj = []

        for a, b in trust:
            adj[a].append(b)

        # Find people who trust nobody
        for i in range(1, n+1):
            if len(adj[i]) == 0:
                current_adj.append(i)

        if len(current_adj) == 0:
            return -1

        # Check whether everyone else trusts the candidate
        for candidate in current_adj:
            count = 0

            for i in range(1, n+1):
                if i != candidate and candidate in adj[i]:
                    count += 1

            if count == n-1:
                return candidate

        return -1
