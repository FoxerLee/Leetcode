class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        char_point = collections.defaultdict(tuple)
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i in range(len(board)):
            for j in range(len(board[i])):
                char_point[board[i][j]] = (i, j)
                
        ans = ""
        cur_point = (0, 0)
        pre_char = ""
        jump = False
        
        while target != "":
            char = target[0]
            target = target[1:]
            if char == 'z' and pre_char != 'u' and pre_char != 'z':
                char = 'u'
                target = 'z' + target
                jump = True
            
            
            next_point = char_point[char]
            
            hor = next_point[0] - cur_point[0]
            ver = next_point[1] - cur_point[1]
            
            if hor < 0:
                ans += "".join(["U" for _ in range(-hor)])
            else:
                ans += "".join(["D" for _ in range(hor)])    
            if ver < 0:
                ans += "".join(["L" for _ in range(-ver)])
            else:
                ans += "".join(["R" for _ in range(ver)])
            if jump != True:
                ans += "!"
            else:
                jump = False
            
            cur_point = next_point
            pre_char = char
            
        return ans
