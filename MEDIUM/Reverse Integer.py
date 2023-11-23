class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)
        if number.startswith('-'):
            ans = '-'+number[1:][::-1]
        elif number == '0':
            return 0
        elif number[-1] == '0':
            ans = number[::-1][1:]
        else:
            ans = number[::-1]
        
        if abs(int(ans)) > 2**31:
            return 0
        else:
            return int(ans)