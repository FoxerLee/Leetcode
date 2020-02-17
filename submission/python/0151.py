class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return ""
        words = reversed(s.split(" "))
        
        ans = ""
        for word in words:
            if word != "":
                ans += word + " "
                
        return ans[:-1]
            
