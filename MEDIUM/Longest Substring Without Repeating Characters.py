class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ''
        ans = []
        index = 0
        while index < len(s):
            if s[index] not in a:
                a += s[index]
            else: 
                ans.append(len(a))
                index -= len(a)-1
                a = ''
                a += s[index]
            index += 1
        ans.append(len(a))
        return max(ans)