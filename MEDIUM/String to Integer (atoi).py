class Solution:
    def myAtoi(self, s: str) -> int:
        max_num = 2**31-1
        min_num = -2**31
        ans = []
        symbol = []
        one = 1
        index = 0
        numb = 0
        spaces = 0
        for i in s:
            if i.isnumeric():
                ans.append(i)
            elif i == ' ' and '0' in ans:
                break
            elif i == ' ' and len(ans)>1:
                break
            elif i == ' ' and len(symbol) > 0:
                break
            elif i == ' ':
                index = -100000000
                continue
            elif (i == '-' or i == '+') and '0' in ans:
                break
            elif (i == '-' or i == '+') and len(ans) > 0:
                break
            elif i == '-' or i == '+':
                index += s.find(i)
                symbol.append(i)
            else:
                break
            numb += 1

        if len(symbol)>1:
            return 0
        elif len(symbol) == 1:
            if symbol[0] == '-':
                one *= -1
        
        if index > 1:
            return 0
        if len(ans) == 0:
            return 0
        else:
            number = int(''.join(ans))*one
        if number > max_num:
            return max_num
        elif number < min_num:
            return min_num
        else:
            return number