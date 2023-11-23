class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return int(str(Counter(nums))[9:str(Counter(nums)).index(':')])