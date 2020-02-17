class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        com = strs[0]

        for i in range(1, len(strs)):
            str1 = com
            str2 = strs[i]

            maxNum = 0
            for j in range(min(len(str1), len(str2))):
                if str1[j] == str2[j]:
                    maxNum += 1
                else:
                    break
            com = str1[:maxNum]
        return com
