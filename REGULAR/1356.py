from typing import List


class Solution:
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        @cache
        def countBits(v):
            c = 0
            while v:
                c+=1
                v = v & (v-1)
            return c
        def cmp(v1, v2):
            c1 = countBits(v1)
            c2 = countBits(v2)
            
            if c1<c2:
                return -1
            elif c1>c2:
                return 1
            else:
                if v1 < v2:
                    return -1
                elif v1>v2:
                    return 1
                else:
                    return 0
        
        
        cmp_items_py3 = cmp_to_key(cmp)
        arr.sort(key=cmp_items_py3)
        return arr