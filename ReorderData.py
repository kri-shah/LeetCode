class helper:
    def __init__(self, ident, logs):
        self.ident = ident
        self.logs = logs
    
    def __lt__(self, other):
        if self.logs == other.logs:
            return self.ident < other.ident
        else:
            return self.logs < other.logs

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        digits = [str(i) for i in range(10)]
        
        for log in logs:
            l = log.split(' ')
            if l[1][0] not in digits:
                h = helper(l[0], l[1:])
                letter_logs.append(h)
            else:
                digit_logs.append(log)
            
        letter_logs.sort()
        res = []
        for obj in letter_logs:
            temp = str(obj.ident) + " " + " ".join(obj.logs)
            res.append(temp)
        
        res.extend(digit_logs)
        
        return res
