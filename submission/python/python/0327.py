class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        
        for num in nums:
            cumsum.append(num+cumsum[-1])
            
        def mergeSort(l, r):
            if l == r:
                return 0
            
            mid = (l+r)//2
            ans = mergeSort(l, mid) + mergeSort(mid+1, r)
            
            i = j = mid + 1
            for left in cumsum[l:mid+1]:
                while i <= r and cumsum[i] - left < lower:
                    i += 1
                while j <= r and cumsum[j] - left <= upper:
                    j += 1
                    
                ans += j - i
                
            cumsum[l:r+1] = sorted(cumsum[l:r+1])
            return ans
        
        return mergeSort(0, len(cumsum)-1)
