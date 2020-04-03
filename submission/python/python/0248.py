class Solution:
# @param {string} low
# @param {string} high
# @return {integer}
    def strobogrammaticInRange(self, low, high):
        a=self.below(high)
        b=self.below(low,include=False)
        return a-b if a>b else 0

    '''
    get how many strobogrammatic numbers less than n
    '''
    def below(self,n,include=True):
        res=0
        for i in range(1,len(n)):
            res+=self.number(i)
        l=self.strobogrammatic(len(n))
        '''
        filter num larger than n and start with 0
        '''
        if include:
            l=[num for num in l if (len(num)==1 or num[0]!='0') and num<=n]
        else:
            l=[num for num in l if (len(num)==1 or num[0]!='0') and num<n]
        return res+len(l)

    '''
    get strobogrammatic numbers with length l
    number start with 0 would be included
    '''
    def strobogrammatic(self,l):
        res=[]
        if l==1:
            return ['0','1','8']
        if l==2:
            return ['00','11','69','96','88']
        for s in self.strobogrammatic(l-2):
            res.append('0'+s+'0')
            res.append('1'+s+'1')
            res.append('6'+s+'9')
            res.append('8'+s+'8')
            res.append('9'+s+'6')
        return res

    '''
    get number of strobogrammatic numbers of length l
    '''
    def number(self,l):
        if l==0:
            return 0
        '''
        If l is an even number, the first digit has four choices (1,6,8,9). digits 
        at other position have five choices(0,1,6,8,9)
        '''
        if l%2==0:
            return 4*(5**(l/2-1))

        elif l==1:
            return 3
        else:
            return 3*(5**(l/2-1))*4
