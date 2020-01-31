class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        send_str = ""
        for s in strs:
            len_s = len(s)
            len_int = len(str(len_s))
            send_str += '0'*(4-len_int)+str(len_s)+s
            
        return send_str

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        receive_strs = []
        p = 0
        while p < len(s):
            len_s = int(s[p:p+4])
            ss = s[p+4:p+len_s+4]
            receive_strs.append(ss)
            p = p+len_s+4
            
        
        return receive_strs
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
