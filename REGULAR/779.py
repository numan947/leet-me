class Solution(object):
    def kthGrammar(self, n, k):
        cur = 0
        l, r = 1, 2**(n-1)
        for _ in range(n-1):
            mid = (l+r)//2
            if k <= mid:
                r = mid
            else:
                l = mid+1
                cur = 0 if cur else 1
        return cur