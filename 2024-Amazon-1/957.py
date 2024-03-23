from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # after day 1
        memo = {}
        first_day = [0]
        for i in range(1, len(cells)-1):
            if cells[i-1] == cells[i+1]:
                first_day.append(1)
            else:
                first_day.append(0)
        first_day.append(0)
        cells = first_day
        memo[0] = (''.join([str(c) for c in cells])) #  0 --> day 1, 1 --> day 2
            
        
        for day in range(1,n+1):
            nxt_day = [0]
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    nxt_day.append(1)
                else:
                    nxt_day.append(0)
            nxt_day.append(0)
            cells = nxt_day
            int_format = (''.join([str(c) for c in cells]))
            if int_format in memo.values():
                break
            memo[day] = int_format
        
        ans = memo[(n-1)%len(memo)]
        ans = [int(c) for c in ans]
        return ans

s = Solution()
print(s.prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], n = 7))
print(s.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 1000000000))
