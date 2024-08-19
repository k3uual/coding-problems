from typing import List

class neighborSum:
    arr = List[List[int]]
    ref = {}
    res = []
    def __init__(self, grid: List[List[int]]):
        self.arr = grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.ref[grid[i][j]] = [i,j]

    def adjacentSum(self, value: int) -> int:
        if(self.ref.get(value)):
            loc = self.ref.get(value)
            sum = 0
            if(loc[1]-1 >= 0):
                sum += self.arr[loc[0]][loc[1]-1]
            if(loc[0]-1 >= 0):
                sum += self.arr[loc[0]-1][loc[1]]
            if(loc[1]+1 < len(self.arr)):
                sum += self.arr[loc[0]][loc[1]+1]
            if(loc[0]+1 < len(self.arr[loc[0]])):
                sum += self.arr[loc[0]+1][loc[1]] 
            self.res.append(sum)
        else:
            self.res.append(None)
        print(self.res)

    def diagonalSum(self, value: int) -> int:
        if(self.ref.get(value)):
            loc = self.ref.get(value)
            sum = 0
            if(loc[0]-1 >= 0 and loc[1]-1 >= 0):
                sum += self.arr[loc[0]-1][loc[1]-1]
                print(self.arr[loc[0]-1][loc[1]-1])
            if(loc[0]+1 < len(self.arr[loc[0]]) and loc[1]-1 >= 0):
                sum += self.arr[loc[0]+1][loc[1]-1]
                print(self.arr[loc[0]+1][loc[1]-1]) 
            if(loc[0]-1 >= 0 and loc[1]+1 < len(self.arr)):
                sum += self.arr[loc[0]-1][loc[1]+1]
                print(self.arr[loc[0]-1][loc[1]+1]) 
            if(loc[0]+1 < len(self.arr[loc[0]]) and loc[1]+1 < len(self.arr)):
                sum += self.arr[loc[0]+1][loc[1]+1]
                print(self.arr[loc[0]+1][loc[1]+1])
            self.res.append(sum)
        else:
            self.res.append(None)
        print(self.res) 
    
s = neighborSum([[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]])
s.adjacentSum(15)


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
