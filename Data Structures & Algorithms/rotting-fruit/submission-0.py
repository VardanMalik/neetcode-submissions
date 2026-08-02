class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        fresh = 0
        time = 0
        q = deque()
        def bfs(r,c):
            if (r<0 or r==rows or
                c<0 or c==cols or
                grid[r][c]==0 or
                (r,c) in visited):
                return
            visited.add((r,c))
            q.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    visited.add((r,c))
                    q.append([r,c])
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while q:
            for i in range(len(q)):
                r,c  = q.popleft()
                if grid[r][c]==1:
                    fresh-=1
                grid[r][c]==2
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r, c-1)
            time +=1
        return time-1 if fresh==0 else -1

