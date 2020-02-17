class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        connect = [(sr, sc)]
        
        startColor = image[sr][sc]
        checked = set()
        while connect:
            now = connect.pop(0)
            checked.add(now)
            image[now[0]][now[1]] = newColor
            for step in steps:
                r = now[0] + step[0]
                c = now[1] + step[1]
                if 0 <= r < len(image) and 0 <= c < len(image[0]):
                    if image[r][c] == startColor and (r,c) not in checked:
                        
                        connect.append((r, c))
                
        return image
