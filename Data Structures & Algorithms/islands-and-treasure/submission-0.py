class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        #first find all zeros
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visit.add((r,c))

        def add_cell(r, c):
            if ((r < 0) or (c < 0) or
                (r >= rows) or (c >= cols) or
                ((r,c) in visit) or 
                (grid[r][c] == -1) 
            ):
                return
            queue.append([r,c])
            visit.add((r,c))


        #BFS on all zeros simultaneously
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist

                add_cell(r+1,c)
                add_cell(r-1,c)
                add_cell(r,c+1)
                add_cell(r ,c-1)

            dist+=1

    
