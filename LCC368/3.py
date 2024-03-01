from typing import List
import heapq
class Solution:
    
    def checkCompliant(self, bottleneck, value):
        return value <= bottleneck+1
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        countValues = {}
        
        for n in nums:
            countValues[n] = countValues.get(n, 0) + 1
        
        bottleneck = len(nums)
        max_heap = []
        for k,v in countValues.items():
            bottleneck = min(bottleneck, v)
            max_heap.append(-v)
        
        print(countValues)
        heapq.heapify(max_heap)
        
        while True:
            max_value = -max_heap[0]
            if max_value <= bottleneck+1:
                break
            else:
                heapq.heappop(max_heap)
                
                val1, val2 = bottleneck, max_value - bottleneck
                vc1,vc2 = self.checkCompliant(bottleneck, val1), self.checkCompliant(bottleneck, val2)
                
                if not(vc1 and vc2):                
                    for v in range(bottleneck+1, (max_value//2)+1):
                        tmpv1, tmpv2 = v, max_value-v
                        tmpvc1, tmpvc2 = self.checkCompliant(bottleneck, tmpv1), self.checkCompliant(bottleneck, tmpv2)
                        if tmpvc1 and tmpvc2:
                            val1, val2 = tmpv1, tmpv2
                            break
                bottleneck = min(bottleneck, val1, val2)
                heapq.heappush(max_heap, -val1)
                heapq.heappush(max_heap, -val2)
                        
        return len(max_heap)


s = Solution()

sol = s.minGroupsForValidAssignment([3,2,3,2,3])
print(sol)
sol = s.minGroupsForValidAssignment([10,10,10,3,1,1])
print(sol)
sol = s.minGroupsForValidAssignment([1,1,3,3,1,1,2,2,3,1,3,2])
print(sol)
sol = s.minGroupsForValidAssignment([2,3,2,2,2])
print(sol)
sol = s.minGroupsForValidAssignment([1,1,2,1,1,3,2,1,2,2,3,1])
print(sol)

sol = s.minGroupsForValidAssignment([2,2,2,2,2,1,2])
print(sol)