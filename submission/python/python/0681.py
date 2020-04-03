class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = sorted(time.replace(':', ''))
        minNumber = digits[0]
        for digit in digits:
                if time[4] < digit:
                        return time[:4] + digit
        for digit in digits:
                if time[3] < digit and digit < '6':
                        return time[:3] + digit + minNumber
        for digit in digits:
                if time[1] < digit and int(time[0] + digit) < 24:
                        return time[0] + digit + ':' + minNumber * 2
        return minNumber * 2 + ':' + minNumber * 2
            
