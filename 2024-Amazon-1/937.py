from curses.ascii import isdigit
from functools import cmp_to_key
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []# (id, contents)
        digit_logs = []
        
        for log in logs:
            splitted = log.split(" ")
            id = splitted[0]
            content1 = splitted[1]
            
            if content1[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((id, " ".join(splitted[1:])))
                
        def compare(a, b):
            if a[1] == b[1]:
                if a[0] < b[0]:
                    return -1
                else:
                    return 1
            else:
                if a[1]<b[1]:
                    return -1
                else:
                    return 1
        

        letter_logs = sorted(letter_logs, key=cmp_to_key(compare))
        
        letter_logs = [l[0]+" "+l[1] for l in letter_logs]
        
        return letter_logs + digit_logs

s = Solution()

print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))