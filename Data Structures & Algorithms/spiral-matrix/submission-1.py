class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #len(matrix) = num of rows
        ans = []
        while matrix:
            ans+=matrix[0]
            matrix = matrix[1:]
            if matrix:
                for n in matrix:
                    if n:
                        ans.append(n.pop())
            if matrix:
                ans+=matrix[-1][::-1]
                matrix.pop()
            if matrix:
                for n in matrix[::-1]:
                    if n:
                        ans.append(n.pop(0))
        return ans