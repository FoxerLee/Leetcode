class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cells = tuple(cells)
        loop_cells = {}
        states = []
        day = 0
        
        while cells not in loop_cells:
            if day == N:
                return cells
            
            states.append(cells)
            loop_cells[cells] = day
            day += 1
            
            tmp = [0]
            for i in range(1, len(cells)-1):
                tmp += [1] if cells[i-1] == cells[i+1] else [0]
            tmp += [0]
            cells = tuple(tmp)
            
        loop_begin = loop_cells[cells]
        loop = day - loop_begin
        
        return states[loop_begin+(N-loop_begin)%loop]
