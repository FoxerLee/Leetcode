class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        integers = collections.defaultdict(int)
        for num in arr:
            integers[num] += 1
            
        sizes = sorted(integers.values())
        remove_size, half_size = 0, len(arr)/2
        
        ans, i = 0, len(sizes)-1
        while remove_size < half_size:
            ans += 1
            remove_size += sizes[i]
            i -= 1
            
        return ans
        
