# DFS
class Solution:
   def dfs(self, grid, row, col):
      grid[row][col] = '0'
      if row-1 >= 0 and grid[row-1][col] == '1':
         self.dfs(grid, row-1, col)
      if col+1 < self.n and grid[row][col+1] == '1':
         self.dfs(grid, row, col+1)
      if row+1 < self.m and grid[row+1][col] == '1:
         self.dfs(grid, row+1, col)
      if col-1 >= 0 and grid[row][col-1] == '1':
         self.dfs(grid, row, col-1)
         
   def numIslands(self, grid: List[List[str]]) -> int:
      self.m = len(grid)
      if not self.m:
         return 0
      self.n = len(grid[0])
      
      num_islands = 0
      for i in range(self.m):
         for j in range(self.n):
            if grid[i][j] == '1':
               num_islands += 1
               self.dfs(grid, i, j)
               
      return num_islands
    
    
# BFS
import queue

class Solution:
   def numIslands(self, grid: List[List[str]]) -> int:
      self.m = len(grid)
      if not self.m:
         return 0
      self.n = len(grid[0])
      
      num_islands = 0
      for i in range(self.m):
         for j in range(self.n):
            if grid[i][j] == '1':
               num_islands += 1
               grid[i][j] = '0'
               neighbors = queue.Queue()
               neighbors.put((i,j))
               while not neighbors.empty():
                  row, col = neighbors.get()
                  if row-1 >= 0 and grid[row-1][col] == '1':
                     neighbors.put((row-1, col))
                     grid[row-1][col] = '0'
                  if row+1 < self.m and grid[row+1][col] == '1':
                     neighbors.put((row+1, col))
                     grid[row+1][col] = '0'
                  if col-1 >= 0 and grid[row][col-1] == '1':
                     neighbors.put((row, col-1))
                     grid[row][col-1] = '0'
                  if col+1 < self.n and grid[row][col+1] == '1':
                     neighbors.put((row, col+1))
                     grid[row][col+1] = '0'
      return num_islands
