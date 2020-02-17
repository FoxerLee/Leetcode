class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        s1tos2 = {}
        
        if len(set(str2)) == 26 and str1 != str2:
            return False
        
        for i in range(len(str1)):
            if str1[i] in s1tos2:
                if s1tos2[str1[i]] != str2[i]:
                    return False
            else:
                s1tos2[str1[i]] = str2[i]
                
        return True
