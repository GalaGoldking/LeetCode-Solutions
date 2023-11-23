class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        columns = [[] for i in range(numRows)]
        col = 0
        for char in s:
            columns[col].append(char)
            if col == 0:
                step = 1
            elif col == numRows - 1:
                step = -1
            col += step
        
        ans = ''
        for column in columns:
            ans += ''.join(column)
        return ans