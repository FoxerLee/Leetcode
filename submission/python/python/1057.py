class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                distances.append([dis, i, j])
                
        
        distances = sorted(distances)
        
        ans = [0 for _ in range(len(workers))]
        w_used = [0 for _ in range(len(workers))]
        b_used = [0 for _ in range(len(bikes))]
        cnt = 0
        for dis in distances:
            w_i = dis[1]
            b_i = dis[2]
            
            if w_used[w_i] == 0 and b_used[b_i] == 0:
                w_used[w_i] = 1
                b_used[b_i] = 1
                ans[w_i] = b_i
                cnt += 1
            
            if cnt > len(workers):
                break
        return ans
