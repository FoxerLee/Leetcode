class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = "".join(S.split("-"))
        a = len(s)
        l = list(s)
        
        if a % K ==0:
            ans = "".join(j + "-" * (i%K == (K-1)) for i,j in enumerate(l))
        else:
            f = a%K
            ans = "".join(l[0:f])+ "-" + "".join(j + "-" * (i%K == (K-1)) for i,j in enumerate(l[f:]))     
        return ans.strip("-").upper()
