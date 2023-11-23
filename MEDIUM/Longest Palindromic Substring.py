class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = []
        start = 0
        while start < len(s):
            for i in range(len(s), 0+start, -1):
                a = s[start:i]
                if len(a) == 1:
                    continue
                elif a == a[::-1]:
                    ans.append(a)
            start += 1
        if len(ans) == 0:
            return s[0]
        else:
            return sorted(ans, key=len)[-1]