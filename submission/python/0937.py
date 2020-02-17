class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = [i for i in logs if not i[-1].isdigit()]
        letter_logs = sorted(letter_logs, key = lambda x: (x[x.find(' '):], x[0:x.find(' ')]))
        digit_logs = [i for i in logs if i[-1].isdigit()]
        
        return letter_logs + digit_logs
