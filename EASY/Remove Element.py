class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
            nums.append('_')
        ans = len(nums)-nums.count('_')
        return ans