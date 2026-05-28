class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        hashMap = defaultdict(list)
        for n1, n2 in edges:
            hashMap[n1].append(n2)
            hashMap[n2].append(n1)
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for j in hashMap[i]:
                if j== prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n==len(visited)