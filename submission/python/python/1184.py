class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # clockwise
        tmp = start
        clock = 0
        while tmp != destination:
            clock += distance[tmp]
            tmp += 1
            if tmp == len(distance):
                tmp = 0
        
        #counterclockwise
        tmp = start 
        counterclock = 0
        while tmp != destination:
            tmp -= 1
            if tmp == -1:
                tmp = len(distance) - 1
            counterclock += distance[tmp]
        
        return min(clock, counterclock)
