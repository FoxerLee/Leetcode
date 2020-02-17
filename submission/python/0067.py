class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            miao = a
            a = b
            b = miao
        re_a = a[::-1]
        re_b = b[::-1]
        
        leng = min(len(re_a), len(re_b))
        
        temp = 0
        result = ""
        for i in range(leng):
            if re_a[i] == '0' and re_b[i] == '0':
                if temp == 0:
                    result += '0'
                if temp == 1:
                    result += '1'
                    temp = 0
            if (re_a[i] == '1' and re_b[i] == '0') or (re_a[i] == '0' and re_b[i] == '1'):
                if temp == 1:
                    temp = 1
                    result += '0'
                if temp == 0:
                    result += '1'
            if re_a[i] == '1' and re_b[i] == '1':
                if temp == 1:
                    result += '1'
                    temp = 1
                if temp == 0:
                    result += '0'
                    temp = 1
        
        for j in range(leng, len(re_b)):
            if re_b[j] == '0' and temp == 0:
                result += '0'
            if (temp == 1 and re_b[j] == '0'):
                result += '1'
                temp = 0
            if (temp == 0 and re_b[j] == '1'):
                result += '1'
            if (temp == 1 and re_b[j] == '1'):
                result += '0'
                temp = 1
        
        if temp == 1:
            result += '1'
        
        result = result[::-1]

        
        return result
        
            
