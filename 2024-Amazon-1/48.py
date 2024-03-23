from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L,R = 0, len(matrix[0])-1
        T,B = 0, len(matrix)-1
        while L<R:   
            for i in range(R-L):
                tmp = matrix[T][L+i]
                matrix[T][L+i] = matrix[B-i][L]
                matrix[B-i][L] = matrix[B][R-i]
                matrix[B][R-i] = matrix[T+i][R]
                matrix[T+i][R] = tmp
            L+=1
            R-=1
            T+=1
            B-=1