class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == []:   
            return 0
        
        # intervals.sort(key=lambda x: x[0])
        
        start = [x[0] for x in intervals]
        start.sort()
        end = [x[1] for x in intervals]
        end.sort()
        
        start_p = 0
        end_p = 0
        
        used_room = 0
        while start_p < len(start):
            if start[start_p] >= end[end_p]:
                end_p += 1
                used_room -= 1
            
            start_p += 1
            used_room += 1
        
        
        return used_room
        
