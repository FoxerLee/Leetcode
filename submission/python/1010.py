class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        module = [0 for _ in range(60)]
        
        for t in time:
            m = t % 60
            module[m] += 1
        ans = 0   
        for i in range(1, 30):
            ans += module[i] * module[60-i]
            
        ans += int((module[30] * (module[30]-1)) / 2)
        ans += int((module[0] * (module[0]-1)) / 2)
        return ans
