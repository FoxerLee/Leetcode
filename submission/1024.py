class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [T+1 for _ in range(T+1)]
        
        dp[0] = 0
        
        for i in range(len(dp)):
            for c in clips:
                if c[0] <= i and c[1] >= i:
                    dp[i] = min(dp[i], dp[c[0]]+1)
                    
        return dp[T] if dp[T] != T+1 else -1
