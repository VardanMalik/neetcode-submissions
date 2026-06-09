class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, destination in tickets:
            adj[src].append(destination)
        res = []
        def dfs(src):
            while adj[src]:
                newAdj = adj[src].pop()
                dfs(newAdj)
            res.append(src)
        dfs("JFK")
        return res[::-1]