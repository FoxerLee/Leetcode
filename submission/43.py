class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_dict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        
        ans1 = 0
        num1 = reversed(num1)
        tmp = 1
        for n in num1:
            ans1 += num_dict[n]*tmp
            tmp *= 10
        
        ans2 = 0
        num2 = reversed(num2)
        tmp = 1
        for n in num2:
            ans2 += num_dict[n]*tmp
            tmp *= 10
        
        
        
        return str(ans1*ans2)
