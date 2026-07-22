from collections import deque

class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2147483647

        gates = deque() # [ [row, col, distanceFromGate], ... ]
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    gates.append([i, j, 0])
        
        rows, cols = len(rooms), len(rooms[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while gates:
            row, col, distance = gates.popleft()

            for r, c in dirs:
                newRow, newCol, newDistance = row + r, col + c, distance + 1
                if (newRow < 0 or newRow == rows or newCol < 0 or newCol == cols
                    or rooms[newRow][newCol] != inf):
                        continue
                rooms[newRow][newCol] = newDistance
                gates.append([newRow, newCol, newDistance])
            
            
        

