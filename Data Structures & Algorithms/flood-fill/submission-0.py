from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        curr = image[sr][sc]
        q.append([sr, sc])
        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]

        while q:
            if curr == color:
                break

            x, y = q.popleft()
            if image[x][y] == curr:
                image[x][y] = color
            
            for changeX, changeY in dirs:
                newX, newY = x + changeX, y + changeY
                if (newX > -1 and newX < len(image) and 
                    newY > -1 and newY < len(image[0]) and 
                    image[newX][newY] == curr):
                    q.append([newX, newY])
        
        return image
