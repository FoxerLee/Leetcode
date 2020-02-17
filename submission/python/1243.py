class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        # end_flag = True
        
        while True:
            end_flag = True
            new_arr = arr[:]
            for i in range(1, len(arr)-1):
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    new_arr[i] = arr[i] - 1
                    end_flag = False
                elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    new_arr[i] = arr[i] + 1
                    end_flag = False
            
            arr = new_arr[:]
            if end_flag:
                break
            
        return arr
                
            
