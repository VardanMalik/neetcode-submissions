class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src,dest in tickets:
            adj[src].append(dest)
        res = []
        def dfs(src):
            while adj[src]:
                nextAdj = adj[src].pop()
                dfs(nextAdj)
            res.append(src)
        dfs("JFK")
        return res[::-1]